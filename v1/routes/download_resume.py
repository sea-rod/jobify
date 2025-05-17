from fastapi.responses import FileResponse,StreamingResponse
from fastapi import APIRouter,Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from utils.file_utils import download_file
from services.supabase_config import supabase
import io

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/download-resume")
def download_resume(token:Annotated[str,Depends(oauth2_scheme)]):
    try:
        uid = supabase.auth.get_user(token).user.id
        print(uid)
        path = f"{uid}/resume.md"
        res = download_file(path,token)
        file_bytes = io.BytesIO(res['message'])
        return StreamingResponse(file_bytes, media_type="application/octet-stream", headers={
            "Content-Disposition": f"attachment; filename=resume.md"
        })
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail=str(e))