from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os


SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Cria o motor do banco de dados, é o conecta com o banco
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Sessão de banco de dados, é quem vai executar as queries
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos declarativos
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()