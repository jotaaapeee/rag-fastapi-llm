import streamlit as st
import requests

st.set_page_config(page_title="RAG Chat", layout="centered")

st.title("RAG Chat com LLM Local")

question = st.text_input("Pergunta:")

if st.button("Enviar") and question:
    with st.spinner("Pensando..."):
        response = requests.post(
            "http://127.0.0.1:8000/ask",
            params={"question": question}
        )

        if response.status_code == 200:
            st.success("Resposta:")
            st.write(response.json()["answer"])
        else:
            st.error("Erro na API")