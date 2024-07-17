import chromadb
from app.core.config import client_openai, EMBEDDING_MODEL
from app.services.chunk import chunk_document
import docx2txt
import os
from app.services.openai_service import create_embedding

client_chroma = chromadb.Client()
collection = client_chroma.get_or_create_collection(name="document_chunks")

def process_document(content):
    with open("temp.docx", "wb") as f:
        f.write(content)
    document_text = docx2txt.process("temp.docx")
    os.remove("temp.docx")

    chunks = chunk_document(document_text)
    for i, chunk in enumerate(chunks):
        embedding = create_embedding(chunk)
        collection.add(documents=[chunk], metadatas=[{"chunk_id": i}], ids=[str(i)], embeddings=[embedding])

def retrieve_context(question):
    embedding = create_embedding(question)
    results = collection.query(query_embeddings=[embedding], n_results=1)
    if results['documents']:
        return results['documents'][0]
    else:
        return "No relevant context found."
