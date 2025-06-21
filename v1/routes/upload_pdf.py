# Copyright 2025 Seamus.F.Rodrigues
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from fastapi import UploadFile, Depends
from fastapi import APIRouter
from typing import Annotated
from fastapi.exceptions import HTTPException
from core import resume_parser
from services.supabase_config import supabase
from utils.file_utils import upload_to_supabase
from fastapi.security import OAuth2PasswordBearer
from services.extract_skills import extract_skills, insert_skills
import os


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
        raise HTTPException(status_code=400, detail="Invalid PDF format")

    if len(content) > MAX_FILE_SIZE_MB * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File too large")

    uid = supabase.auth.get_user(token).user.id
    text = await resume_parser.extract_text(content)
    skills = extract_skills(text)
    res = insert_skills(skills, uid)
    print("skills:", res)

    if upload_to_supabase(token, text, f"{uid}/resume.md"):
        return {"message": "Upload successful"}

    raise HTTPException(status_code=500, detail="Upload Failed")
