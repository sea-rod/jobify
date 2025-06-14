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

from fastapi.responses import StreamingResponse
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from utils.file_utils import download_file
from services.supabase_config import supabase
from services.convert_to_markdown import markdown_to_pdf

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/download-resume")
def download_resume(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        uid = supabase.auth.get_user(token).user.id
        print(uid)
        path = f"{uid}/resume.md"
        res = download_file(path, token)
        buffer = markdown_to_pdf(res["message"].decode())
    
        return StreamingResponse(
            buffer,
            media_type="application/octet-stream",
            headers={"Content-Disposition": f"attachment; filename=resume.pdf"},
        )
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail=str(e))
