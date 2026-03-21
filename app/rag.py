import psycopg2
import ollama
from app.embeddings import get_embedding

conn = psycopg2.connect(
    dbname="rag",
    user="postgres",
    password="postgres",
    host="localhost"
)

def search_docs(query):

    emb = get_embedding(query)

    cur = conn.cursor()

    emb_str = "[" + ",".join(map(str, emb)) + "]"

    cur.execute("""
        SELECT content
        FROM documents
        ORDER BY embedding <-> %s::vector
        LIMIT 3
    """, (emb_str,))

    results = cur.fetchall()

    return "\n".join(r[0] for r in results)


def ask_rag(question):

    context = search_docs(question)

    prompt = f"""
    Answer using the context below.

    Context:
    {context}

    Question:
    {question}
    """

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]