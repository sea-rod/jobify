from fastapi import UploadFile, Depends
from fastapi import APIRouter
from typing import Annotated
from fastapi.exceptions import HTTPException
from core import resume_parser
from services.supabase_config import supabase
from utils.file_utils import upload_to_supabase
import os
from fastapi.security import OAuth2PasswordBearer


SUPABASE_URL = os.environ.get("SUPABASE_URL")
BUCKET_NAME = os.environ.get("BUCKET_NAME")
MAX_FILE_SIZE_MB = 5

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()


def is_valid_pdf(file_bytes: bytes) -> bool:
    return file_bytes.startswith(b"%PDF-")


@router.post("/upload-resume")
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

    
    if upload_to_supabase(token, text, f"{uid}/resume.md"):
        return {"message": "Upload successful"}
    
    raise HTTPException(status_code=500, detail="Upload Failed")

