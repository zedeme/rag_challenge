# rag_challenge

### README for RAG Challenge

## Project Overview

This project is a simple Retrieval-Augmented Generation (RAG) system built with FastAPI, OpenAI, and ChromaDB. The system allows users to interact with a language model (LLM) to generate responses based on a provided document.

## Features

- **Upload a Document**: Upload a .docx file, which will be processed and stored in ChromaDB.
- **Ask Questions**: Ask questions about the content of the uploaded document. The system will retrieve the relevant context from ChromaDB and generate a response using the OpenAI language model.

## Project Structure

```
rag_challenge/
│
├── main.py
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── endpoints/
│   │   │   ├── __init__.py
│   │   │   ├── ask.py
│   │   │   ├── upload.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── chunk.py
│   │   ├── openai_service.py
│   │   ├── chroma_service.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── request.py
```

## Setup and Installation

### Prerequisites

- Python 3.8+
- pip (Python package installer)
- OpenAI API Key

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/rag_challenge.git
   cd rag_challenge
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

5. **Run the Application**

   ```bash
   uvicorn main:app --reload
   ```

   The application will be available at `http://localhost:8000`.

## Usage

### Upload a Document

To upload a .docx document:

- **Endpoint**: `POST /upload`
- **Form Data**: `file` (the .docx file)

#### Example using `curl`

```bash
curl -X POST "http://localhost:8000/upload" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@path_to_your_document.docx"
```

### Ask a Question

To ask a question about the content of the uploaded document:

- **Endpoint**: `POST /ask`
- **JSON Body**: `{"user_name": "John Doe", "question": "Who is Zara?"}`

#### Example using `curl`

```bash
curl -X POST "http://localhost:8000/ask" -H "accept: application/json" -H "Content-Type: application/json" -d '{
  "user_name": "John Doe",
  "question": "Who is Zara?"
}'
```

## Project Files Description

- **main.py**: The entry point of the application. It initializes the FastAPI app and includes the routers.
- **app/api/endpoints/ask.py**: Contains the endpoint for asking questions.
- **app/api/endpoints/upload.py**: Contains the endpoint for uploading documents.
- **app/core/config.py**: Configuration file for the OpenAI client.
- **app/services/chunk.py**: Service for chunking the document.
- **app/services/openai_service.py**: Service for interacting with the OpenAI API.
- **app/services/chroma_service.py**: Service for processing documents and managing embeddings in ChromaDB.
- **app/models/request.py**: Contains the Pydantic model for the request.
