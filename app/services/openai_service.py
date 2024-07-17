from app.core.config import client_openai, EMBEDDING_MODEL
from polyglot.detect import Detector

def create_embedding(input_text):
    embedding_response = client_openai.embeddings.create(input=[input_text], model=EMBEDDING_MODEL)
    return embedding_response.data[0].embedding

def generate_response(question, context):
    detector = Detector(question)
    language = detector.language.code

    response = client_openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that always responds in the same language as the question (English, Spanish, Portuguese). Your answer must be in one sentence. Your answer must include emojis that summarize the content of the answer. Your answer must be in third person."},
            {"role": "user", "content": f"Context: {context}\nQuestion: {question}\nAnswer's Language: {language} \n\nAnswer (Remember to follow the instructions exactly and the expected language):"},
        ],
        max_tokens=4096
    )

    return response.choices[0].message.content

