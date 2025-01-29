from fastapi import FastAPI

app= FastAPI()              #Executar terminal - fastapi dev (caminho arquivo) 
                            #-> sobe um servidor local para executar


@app.get('/')    #'/' é a raiz do site
def read_root():
    return {'message' : 'Hello armando'}

@app.get('/world')
def read_root():
    return {'message' : 'Hello world'}


