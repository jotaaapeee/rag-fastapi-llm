from sqlalchemy import create_engine

DB_URL = "postgresql://postgres:postgres@localhost:5432/rag"

engine = create_engine(DB_URL)