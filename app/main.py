from fastapi import FastAPI
# from rag import ask_rag
from app.rag import ask_rag

app = FastAPI()

@app.get("/")
def root():
    return {"status": "RAG API running"}

@app.post("/ask")
def ask(question: str):
    # print(question)

    answer = ask_rag(question)

    return {
        "question": question,
        "answer": answer
    }