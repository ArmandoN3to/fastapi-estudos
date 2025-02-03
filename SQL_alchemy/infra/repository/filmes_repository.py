from infra.configs.connection import DBConnectionHandler
from infra.entities.filmes import Filmes

class FilmesRepositoy:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Filmes).all()
            return data
        
    def insert(self,titulo,genero,ano):
        with DBConnectionHandler() as db:
            data_insert = Filmes(titulo=titulo,genero=genero,ano=ano)
            db.add(data_insert)
            db.commit()

    def delete(self,titulo):
        with DBConnectionHandler() as db:
            db.session.query(Filmes).filter(Filmes.titulo==titulo).delete
            db.commit()

    def update(self,titulo,ano):
        with DBConnectionHandler() as db:
            db.query(Filmes).filter(Filmes.titulo ==titulo).update({ "ano":ano })
            db.commit()