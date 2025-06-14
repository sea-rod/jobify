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

from fastapi import FastAPI
from v1.routes import upload_pdf, get_feedback, download_resume, get_jobs


from fastapi.middleware.cors import CORSMiddleware
import os
import dotenv

dotenv.load_dotenv()

ALLOWED_HOST = os.environ.get("ALLOWED_HOST")

origins = [
    "http://localhost:5173",
    "http://localhost:8080",
    ALLOWED_HOST,
]

print(origins)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(upload_pdf.router)
app.include_router(get_feedback.router)
app.include_router(download_resume.router)
app.include_router(get_jobs.router)
