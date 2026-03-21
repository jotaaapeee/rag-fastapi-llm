#!/bin/bash

docker compose up -d
ollama pull nomic-embed-text
ollama 
python app/ingest.py
ollama serve
uvicorn app.main:app --reload