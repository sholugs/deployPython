from firebase_admin import db

def post_user(user):
    if user:
        ref = db.reference('/User')
        ref.push(user)
        return True
    return False

def get_user(username):
    ref = db.reference('/User')
    users = ref.order_by_child('username').equal_to(username).get()
    if users:
        user_id, user_info = users.popitem()
        return {'user_id': user_id, **user_info}
    else:
        return None
    
def find_user(username, password):

    ref = db.reference('/User')
    users = ref.order_by_child('username').equal_to(username).get()
    if users:
        # Verificar la contraseña
        for user in users.values():
            if user['password'] == password:
                return "Succesfully logged in"
            else:
                return "Wrong password"
    else:
        return "The user doesn't exist"
    