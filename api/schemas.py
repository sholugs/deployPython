from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id : Optional[str]
    username : str
    password : str
    email : str
    birthdate : str
    gender : str
    height : str
    weight : str

class Login(BaseModel):
    username : str
    password : str