from infra.repository.filmes_repository import FilmesRepositoy
repo = FilmesRepositoy()
data=repo.select()
repo.insert("Algum Filme",'comedia',2010)
repo.delete('dasda')

print(data)
