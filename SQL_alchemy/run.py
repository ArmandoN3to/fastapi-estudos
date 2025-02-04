from infra.repository.atores_repository import AtoresRepositoy
from infra.repository.filmes_repository import FilmesRepositoy
repo = AtoresRepositoy()
response=repo.select()
# print(response)

repo2=FilmesRepositoy()
response2=repo2.select_drama_filmes()
print(response2)
