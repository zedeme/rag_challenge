from fastapi import FastAPI
from app.api.endpoints import ask, upload

app = FastAPI()

app.include_router(ask.router)
app.include_router(upload.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)