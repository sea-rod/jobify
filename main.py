from fastapi import FastAPI, Request, UploadFile, Form,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from services.resume_feedback import get_resume_feedback,apply_feedback
from services.convert_to_markdown import markdown_to_pdf
from v1.routes import upload_pdf
import os
from pydantic import BaseModel


from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:5173",
    "http://localhost:8080",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(upload_pdf.router)


