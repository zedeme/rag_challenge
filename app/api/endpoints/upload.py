from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.chroma_service import process_document

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    try:
        if file.filename.endswith(".docx"):
            content = await file.read()
            process_document(content)
            return {"status": "Document processed successfully"}
        else:
            raise HTTPException(status_code=400, detail="Invalid file format. Please upload a .docx file.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))