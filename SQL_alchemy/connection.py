from sqlalchemy import create_engine 

engine=create_engine('mysql+pymysql://root:Feiradesantana1!@localhost:3306/cinema')
response = engine.exec_driver_sql('SELECT * FROM filmes;')

for row in response:
    print(row)
    print(row.titulo)
