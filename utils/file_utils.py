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


import os
import requests
import tempfile


from fastapi import HTTPException

SUPABASE_URL = os.environ.get("SUPABASE_URL")
BUCKET_NAME = os.environ.get("BUCKET_NAME")


def download_file(path, token):
    try:
        res = requests.get(
            f"{SUPABASE_URL}/storage/v1/object/{BUCKET_NAME}/{path}",
            headers={
                "Authorization": f"{token}",
            },
        )
        if res.status_code >= 400:
            # logger.error(f"Upload failed: {response.text}")
            raise HTTPException(status_code=500, detail="download failed")

        # logger.info(f"Uploaded file for user {user_id} to {file_path}")
        return {"message": res.content}
    except Exception as e:
        print(e)

def upload_to_supabase(token,text,file_path):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".md") as temp_file:
        temp_file.write(text.encode("utf-8"))
    try:
        response = requests.post(
            f"{SUPABASE_URL}/storage/v1/object/{BUCKET_NAME}/{file_path}",
            headers={
                "Authorization": f"{token}",
                "x-upsert": "true",
            },
            files={"file": open(temp_file.name, "rb")}
        )

        if response.status_code >= 400:
            # logger.error(f"Upload failed: {response.text}")
            raise HTTPException(status_code=500, detail="Upload failed")

        # logger.info(f"Uploaded file for user {user_id} to {file_path}")
        
    except Exception as e:
        print(e)
    finally :
        os.unlink(temp_file.name)
        return True
