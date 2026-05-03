#!/bin/bash

docker compose up -d
ollama pull nomic-embed-text
ollama pull llama3.2
python app/ingest.py
ollama serve
uvicorn app.main:app --reload