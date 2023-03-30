from fastapi import FastAPI
from schemas import User, Login
from firebase.firebase_crud import get_user, find_user, post_user
from fastapi.middleware.cors import CORSMiddleware
import firebase_admin
from firebase_admin import credentials

#Credenciales de firebase
firebase_sdk = credentials.Certificate("./sanva-project-54f54-firebase-adminsdk-km05b-b6e691f9f4.json")

#Referencia a la base de datos
firebase_admin.initialize_app(firebase_sdk,{'databaseURL':'https://sanva-project-54f54-default-rtdb.firebaseio.com/'})


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return ("hola mundo")

@app.post('/user')
async def register_user(user : User):
    print(user)
    try:
        new_user = {
            "username" : user.username,
            "password" : user.password,
            "email" : user.email
        }
        post_user(new_user)
        if new_user:
            return "User successfully registered"
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/user/{username}")
async def get_user_by_email(username : str):
    try:
        find_user = get_user(username)
        if find_user:
            return find_user
        return "User not found"
    except Exception as e:
        return {"error": str(e)}
    
@app.post("/login")
async def log_in_user(user : Login):
    try:
        return find_user(user.username, user.password)
    except Exception as e:
        return {"error" : e}
