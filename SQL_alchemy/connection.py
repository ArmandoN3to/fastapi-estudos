from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import sessionmaker,registry

#Configuraçoes
engine=create_engine('mysql+pymysql://root:{minhasenha}@localhost:3306/cinema')
mapper_registy = registry()
Base = mapper_registy.generate_base()
Session=sessionmaker(bind=engine)
session=Session()

#Entidades
class Filmes(Base):
    __tablename__ = "filmes"

    titulo = Column(String,primary_key=True)
    genero = Column(String,nullable=False)
    ano=Column(Integer,nullable=False)

    def __repr__(self):
        return f"Filme [titulo = {self.titulo}, ano = {self.ano}]"


#SQL

#Delete
session.query(Filmes).filter(Filmes.titulo=="Batman").delete()
session.commit()

#Insert
data_insert = Filmes(titulo="dasda",genero="Acao",ano=2022)
session.add(data_insert)
session.commit()

#Update
session.query(Filmes).filter(Filmes.genero =="Drama").update({ "ano":2000 })
session.commit()
#Select
data_select=session.query(Filmes).all()
print(data_select) 
print(data_select[0].titulo)       #ACESSA O ELEMENTO INTERNO

session.close()