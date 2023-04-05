def user_schema(user) -> dict:
    return {"id": str(user["_id"]),
            "username": user["username"],
            "email": user["email"],
            "password": user["password"],
            "birthdate": user["birthdate"],
            "gender": user["gender"],
            "height": user["height"],
            "weight": user["weight"]
            }


def users_schema(users) -> list:
    return [user_schema(user) for user in users]