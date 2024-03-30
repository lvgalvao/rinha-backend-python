from sqlalchemy import Column, String, Date, ARRAY
from sqlalchemy.dialects.postgresql import UUID
import uuid

from db import Base

class PessoaModel(Base):
    __tablename__ = 'pessoas'
    
    # Definindo as colunas
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    apelido = Column(String(32), nullable=False)
    nome = Column(String(100), nullable=False)
    nascimento = Column(Date, nullable=False)
    stack = Column(ARRAY(String))
