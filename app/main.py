from fastapi import FastAPI
from rag import ask_rag

app = FastAPI()

@app.get("/")
def root():
    return {"status": "RAG API running"}

@app.post("/ask")
def ask(question: str):

    answer = ask_rag(question)

    return {
        "question": question,
        "answer": answer
    }