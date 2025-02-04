from infra.configs.base import Base
from sqlalchemy import Column,String,Integer,ForeignKey

#Entidades
class Atores(Base):
    __tablename__ = "atores"

    id = Column(Integer,primary_key=True)
    nome = Column(String,nullable=False)
    titulo_filme=Column(String,ForeignKey("filmes.titulo"))

    def __repr__(self):
        return f"Atores [nome = {self.nome} Filme [Filme = {self.titulo_filme}] "