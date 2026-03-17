import psycopg2
import ollama
from embeddings import get_embedding

conn = psycopg2.connect(
    dbname="rag",
    user="postgres",
    password="postgres",
    host="localhost"
)

def search_docs(query):

    emb = get_embedding(query)

    cur = conn.cursor()

    cur.execute("""
        SELECT content
        FROM documents
        ORDER BY embedding <-> %s
        LIMIT 3
    """, (emb,))

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
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]