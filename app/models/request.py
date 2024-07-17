from pydantic import BaseModel

class QuestionRequest(BaseModel):
    user_name: str
    question: str