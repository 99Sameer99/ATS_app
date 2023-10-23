from fastapi import APIRouter, status
from fastapi import File, UploadFile
import aiofiles
from typing import List
import shutil
from uuid import uuid4
from src.Utils.config import Config
from fastapi.responses import JSONResponse
from src.Utils.helper import *

upload_router = APIRouter()

@upload_router.post("/single-file")
async def upload_single_file(file: UploadFile = File(...)):
    """
    
    Endpoint to handle single file upload.

    """
    filename = file.filename
    file_extension = filename.split(".")[-1].lower()
    if file_extension == 'pdf':
        file_path = f"{Config.RESUME_DIR}/{str(uuid4())}.pdf"
        with open(file_path, 'wb') as fileobject:
            shutil.copyfileobj(file.file, fileobject)
        

        openai_instance = get_openaicaller_instance()
        openai_instance.handle_pdf_push(file_path = file_path)

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "success",
                "filename": filename,
                "file path": file_path,
            }
        )
    else:
        raise Exception("File extension not allowed")