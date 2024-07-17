from fastapi import APIRouter, HTTPException
from app.models.request import QuestionRequest
from app.services.openai_service import generate_response
from app.services.chroma_service import retrieve_context

router = APIRouter()

@router.post("/ask")
async def ask_question(request: QuestionRequest):
    try:
        context = retrieve_context(request.question)
        response = generate_response(request.question, context)
        return {"answer": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))