from mongoDB.mySchema.userSchema import user_schema
from schemas import User, Login
from mongoDB.client import db

# def post_user(user):
#     if user:
#         ref = db.reference('/User')
#         ref.push(user)
#         return True
#     return False

# make a post_user function to create a new user into the mongodb database

# def post_user(user):
#     if user:
#         db_client.users.insert_one(user)
#         return True
#     return False

# def get_user(username):
#     ref = db.reference('/User')
#     users = ref.order_by_child('username').equal_to(username).get()
#     if users:
#         user_id, user_info = users.popitem()
#         return {'user_id': user_id, **user_info}
#     else:
#         return None
    
# def find_user(username, password):

#     ref = db.reference('/User')
#     users = ref.order_by_child('username').equal_to(username).get()
#     if users:
#         # Verificar la contraseña
#         for user in users.values():
#             if user['password'] == password:
#                 return "Succesfully logged in"
#             else:
#                 return "Wrong password"
#     else:
#         return "The user doesn't exist"

# async def get_user_by_email(email : str):
#     try:
#         find_user = search_user("email", email)
#         if type(find_user) == User:
#             return find_user
#         return "User not found"
#     except Exception as e:
#         return {"error": str(e)}

def search_user(field: str, value):

    try:
        user = db.users.find_one({field: value})
        return User(**user_schema(user)[0])
    except Exception as e:
        return {"error": str(e)}


