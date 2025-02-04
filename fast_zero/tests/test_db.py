from fast_zero.models import User,table_registry

from sqlalchemy import create_engine

def test_create_user():
    engine = create_engine(
       'sqlite:///database.db')
    table_registry.metadata.create_all(engine)

    user=User(username ='Armando',email='armando@mail.com',password='12345')

    assert user.username=='Armando'
