from fast_zero.models import table_registry
from fast_zero.settings import Settings
from sqlalchemy import create_engine

engine = create_engine(Settings().DATABASE_URL)
table_registry.metadata.create_all(engine)
print("Tabelas criadas com sucesso!")