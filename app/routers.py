from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from db import get_db
from schemas import PessoaResponse, PessoaCreate
from typing import List
from crud import criar_pessoa, get_pessoa, contar_pessoas, get_pessoa_por_apelido
from uuid import UUID

router = APIRouter()

@router.post("/pessoa/", response_model=PessoaResponse, status_code=201)
def criar_pessoa_rota(pessoa: PessoaCreate, db: Session = Depends(get_db)):
    return criar_pessoa(db=db, pessoa=pessoa)

@router.get("/pessoas/contagem/", response_model=int)
def contar_pessoas_rota(db: Session = Depends(get_db)):
    return contar_pessoas(db)

@router.get("/pessoa/{pessoa_id}", response_model=PessoaResponse)
def pegar_pessoa_rota(pessoa_id: UUID, db: Session = Depends(get_db)):
    pessoa = get_pessoa(db, pessoa_id=pessoa_id)
    if pessoa is None:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return pessoa

@router.get("/pessoas/por-apelido/", response_model=List[PessoaResponse])
def buscar_pessoa_por_apelido(apelido: str = Query(..., min_length=1), db: Session = Depends(get_db)):
    pessoas = get_pessoa_por_apelido(db, apelido=apelido)
    if not pessoas:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return pessoas
