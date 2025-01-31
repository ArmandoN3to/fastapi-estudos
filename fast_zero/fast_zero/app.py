from fastapi import FastAPI,HTTPException
from fastapi.responses import HTMLResponse 
from http import HTTPStatus
from fast_zero.schemas import Message, UserSchema,UserPublic,UserDB,UserList

app = FastAPI()

database = []

@app.get('/',status_code=HTTPStatus.OK,response_model=Message)#response_model=Message
def read_root():
    return {'message':'Olá mundo!'}

@app.post('/users/',response_model=UserPublic,status_code=HTTPStatus.CREATED) #ele pega a resposta da classe UserPublic em vez do USerSchema
def create_user(user:UserSchema):
    user_with_id = UserDB(id=len(database) + 1,**user.model_dump())

    database.append(user_with_id)

    return user_with_id

#response_class - trocar modelo de validaçao ex: vou trabalhar com JSON ou HTML
#response_model - validaçao exata dos dados 

#Sempre que enviamos o POST o status_code = 201 ou CREATED

@app.get('/users/',response_model=UserList)
def read_users():
    return {'users':database}

@app.put('/users/{user_id}',response_model=UserPublic)
def update_user(user_id: int, user:UserSchema):

    if user_id<1 or user_id>len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        ) 
    user_with_id=UserDB(id=user_id,**user.model_dump())
    database[user_id - 1] = user_with_id

    return user_with_id

@app.delete('/users/{user_id}',response_model=Message)
def delete_user(user_id:int):
    if user_id<1 or user_id>len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        ) 
    
    del database[user_id - 1] 
    return {'message': 'User deleted'}

