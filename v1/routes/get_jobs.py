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


from fastapi.routing import APIRouter
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from services.supabase_config import supabase
from core.job_fetcher import fetch_jobs
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()


@router.get("/jobs")
def get_jobs(token: Annotated[str, Depends(oauth2_scheme)]):
    uid = supabase.auth.get_user(token).user.id
    print(uid)
    res = (
        supabase.table("user_skills").select("skills").eq("user_id", uid).execute()
    )
    skills = res.data[0]["skills"]["technical_skills"]
    job_list = fetch_jobs("pune",skills=skills)
    return job_list
