from fastapi import APIRouter, HTTPException, status
from mongoDB.user import search_user
from schemas import User, Login
from mongoDB.mySchema.userSchema import user_schema, users_schema
from mongoDB.client import db
from bson import ObjectId

app = APIRouter(prefix="/user", tags=["User"], responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}})

@app.get("/", response_model=list[User])
async def index():
    return users_schema(db.users.find())

@app.post("/", response_model=User)
async def post_user(user: User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")

    user_dict = dict(user)
    del user_dict["id"]

    id = db.users.insert_one(user_dict).inserted_id

    new_user = user_schema(db.users.find_one({"_id": id}))

    return User(**new_user)

@app.get("/email/{email}", response_model=User)
async def get_user_by_email(email : str):
    try:
        find_user = search_user("email", email)
        if type(find_user) == User:
            return find_user
        return "User not found"
    except Exception as e:
        return {"error": str(e)}

@app.get("/username/{username}", response_model=User)
async def get_user_by_username(username : str):
    try:
        find_user = search_user("username", username)
        if type(find_user) == User:
            return find_user
        return "User not found"
    except Exception as e:
        return {"error": str(e)}

@app.get("/id/{id}")
async def user(id: str):
    return search_user("_id", ObjectId(id))

@app.put("/id/{id}", response_model=User)
async def user(id: str, user: User):
    found = db.users.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(user)},
        return_document=True
    )
    if found:
        return User(**user_schema(found))
    if not found:
        return {"updated": False}
    
@app.delete("/id/{id}")
async def user(id: str):
    found = db.users.find_one_and_delete({"_id": ObjectId(id)})
    if found:
        return {"deleted": True}
    if not found:
        return {"deleted": False}


@app.post("/login", response_model=User)
async def login(login: Login):
    try:
        find_user = search_user("username", login.username)
        if type(find_user) == User:
            if find_user.password == login.password:
                return find_user
            return "Wrong password"
        return "User not found"
    except Exception as e:
        return {"error": str(e)}
