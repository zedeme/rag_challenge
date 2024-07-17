def chunk_document(document_text, chunk_size=400):
    return [document_text[i:i+chunk_size] for i in range(0, len(document_text), chunk_size)]
