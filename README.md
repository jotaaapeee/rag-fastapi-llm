# FastAPI RAG Demo

RAG project with FastAPI, embeddings and pgvector

SImple Retrieval-Augmented Generation API using:

- FastAPI
- Ollama
- PostgreSQL + pgvector
- Local embeddings

Archtecture:

User Question -> Embedding -> Vector Search -> COntext -> LLM -> Answer

## How to run 

You can use the script.sh, he basically does what you will see down here.

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

docker compose up -d
python app/ingest.py

Downloading model:
sudo snap install ollama
ollama pull nomic-embed-text

Running api:
uvicorn app.main:app --reload
ollama serve