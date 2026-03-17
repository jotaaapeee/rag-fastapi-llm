from embeddings import get_embedding
from database import engine
import psycopg2

conn = psycopg2.connect(
    dbname="rag",
    user="postgres",
    password="postgres",
    host="localhost"
)

cur = conn.cursor()

cur.execute("""
CREATE EXTENSION IF NOT EXISTS vector;
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS documents (
    id SERIAL PRIMARY KEY,
    content TEXT,
    embedding vector(768)
);
""")

with open("data/docs.txt") as f:
    docs = f.readlines()

for doc in docs:
    emb = get_embedding(doc)

    cur.execute(
        "INSERT INTO documents (content, embedding) VALUES (%s, %s)",
        (doc, emb)
    )

conn.commit()