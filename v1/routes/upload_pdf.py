from fastapi import UploadFile, Depends
from fastapi import APIRouter
from typing import Annotated
from fastapi.exceptions import HTTPException
from core import resume_parser
from services.resume_feedback import get_resume_feedback, apply_feedback
from services.supabase_config import supabase
import os
import tempfile
from fastapi.security import OAuth2PasswordBearer
import requests


SUPABASE_URL = os.environ.get("SUPABASE_URL")
BUCKET_NAME = os.environ.get("BUCKET_NAME")
MAX_FILE_SIZE_MB = 5

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


router = APIRouter()


def upload_to_supabase(token,temp_file_path,file_path):
    try:
        response = requests.post(
            f"{SUPABASE_URL}/storage/v1/object/{BUCKET_NAME}/{file_path}",
            headers={
                "Authorization": f"{token}",
                "x-upsert": "true",
            },
            files={"file": open(temp_file_path, "rb")}
        )

        if response.status_code >= 400:
            # logger.error(f"Upload failed: {response.text}")
            raise HTTPException(status_code=500, detail="Upload failed")

        # logger.info(f"Uploaded file for user {user_id} to {file_path}")
        return {"message": "Upload successful", "path": file_path}
    except Exception as e:
        print(e)


def is_valid_pdf(file_bytes: bytes) -> bool:
    return file_bytes.startswith(b"%PDF-")


@router.post("/get-feedback")
async def create_upload_file(
    token: Annotated[str, Depends(oauth2_scheme)], file: UploadFile
):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    content = await file.read()

    if not is_valid_pdf(content):
        raise HTTPException(
            status_code=400, detail="Invalid PDF format"
        )

    if len(content) > MAX_FILE_SIZE_MB * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File too large")

    uid = supabase.auth.get_user(token).user.id
    text = await resume_parser.extract_text(content)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".md") as temp_file:
        temp_file.write(text.encode("utf-8"))
        temp_file_path = temp_file.name
    try:
        response = upload_to_supabase(token, temp_file_path, f"{uid}/resume.md")
    finally:
        os.unlink(temp_file_path)
    return {"response": response}
