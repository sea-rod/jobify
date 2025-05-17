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


from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from services.resume_feedback import get_resume_feedback,apply_feedback
from services.supabase_config import supabase
from utils.file_utils import upload_to_supabase,download_file

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()


from pydantic import BaseModel

class Feedback(BaseModel):
    feedback:list


@router.get("/get-feedback")
def get_feedback(token:Annotated[str,Depends(oauth2_scheme)]):
    uid = supabase.auth.get_user(token).user.id
    print(uid)
    path = f"{uid}/resume.md"
    response = download_file(path,token)
    feedback = get_resume_feedback(response['message'])
    print(feedback)
    return {"feedback":feedback}


@router.post("/apply-feedback")
def apply_feedback_endpoint(token:Annotated[str,Depends(oauth2_scheme)],feedback:Feedback):
    uid = supabase.auth.get_user(token).user.id
    path = f"{uid}/resume.md"
    resume = download_file(path,token)
    updated_resume = apply_feedback(resume,feedback)
    if upload_to_supabase(token,updated_resume,path):
        return {"message": "Feedback applied successfully"}
    
    raise HTTPException(status_code=500, detail="Server Error")