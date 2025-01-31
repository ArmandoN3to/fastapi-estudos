from pydantic import BaseModel

class Message(BaseModel):       #Utilizaçao de schemas 
    message:str     #falando que a response precisa ser str