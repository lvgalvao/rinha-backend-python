from sqlalchemy.orm import Session
from models import PessoaModel
from schemas import PessoaCreate
from typing import Optional

def get_pessoa(db: Session, pessoa_id: int) -> Optional[PessoaModel]:
    return db.query(PessoaModel).filter(PessoaModel.id == pessoa_id).first()

def contar_pessoas(db: Session) -> int:
    return db.query(PessoaModel).count()

def criar_pessoa(db: Session, pessoa: PessoaCreate) -> PessoaModel:
    db_pessoa = PessoaModel(**pessoa.model_dump())
    db.add(db_pessoa)
    db.commit()
    db.refresh(db_pessoa)
    return db_pessoa

def get_pessoa_por_apelido(db: Session, apelido: str) -> list[PessoaModel]:
    return db.query(PessoaModel).filter(PessoaModel.apelido.op('~')(apelido)).all()
