# FastAPI will run with Uvicorn
import uvicorn
from fastapi import FastAPI, HTTPException
from libmongo import LibMongo
from libzeta import LibZeta
from user import User, UserResponse, DeleteResponse, FakeUserResponse, UserUpdate
from faker import Faker
from random import randrange
import re

app = FastAPI()

def run():
    uvicorn.run(app, port=8022)

@app.get("/")
def get_root():
    return {"Hello": "World"}


libmongo = LibMongo(
    "localhost:27017",
    "jose",
    "Ooph7Jahnohch7Hoah3pheejeizuetha",
    "jose"
)

libzeta = LibZeta(
    "http://localhost:3000",
    "aw2Gei9NeePhiel6ohYi1hai",
    "ooT7loh2ohPh6shopaideeX6"
)

def username_constraint(username):
    if not re.match(r"^[A-Za-z_][A-Za-z0-9_]{3,29}$", username):
        raise HTTPException(
            status_code=400,
            detail=f"The username {username} don't use the pattern")
    return True


@app.post("/user", response_model=UserResponse)
def create_user(user: User):
    new_user = None
    try:
        username_constraint(user.username)
        if not libmongo.users.find_one({"username": user.username}):
            user_data = user.dict()
            zeta_data = libzeta.create_user(user.username)
            user_data.update({'zeta': zeta_data})
            new_user = UserResponse.parse_obj(user_data)
            id = libmongo.users.insert(user_data)
        else:
            raise HTTPException(
                status_code=409,
                detail=f"The user with username {user.username} already exists")
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return new_user

@app.get("/user/{username}", response_model=UserResponse)
def get_user(username: str):
    user = None
    try:
        username_constraint(username)
        user_data = libmongo.users.find_one({"username": username})
        if user_data:
            user = UserResponse.parse_obj(user_data)
        else:
            raise HTTPException(
                status_code=404,
                detail=f"The user with username {username} don't exists")
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return user

@app.delete("/user/{username}", response_model=DeleteResponse)
def delete_user(username: str):
    response = False
    try:
        username_constraint(username)
        filters = {"username": username}
        user_data = libmongo.users.find_one(filters)
        if user_data:
            libmongo.users.delete_one(filters)
            deleted = True
        else:
            raise HTTPException(
                status_code=404,
                detail=f"The user with username {username} don't exists")
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return DeleteResponse.parse_obj({'deleted': deleted})

@app.put("/user/{username}", response_model=UserResponse)
def update_user(username: str, user: UserUpdate):
    update_user = None
    try:
        username_constraint(username)
        if libmongo.users.find_one({"username": username}):
            user_data_raw = user.dict()
            user_data = {}
            for key in user_data_raw.keys():
                if user_data_raw[key] is not None:
                    user_data.update({key: user_data_raw[key]})
            if len(user_data.keys()) == 0:
                raise HTTPException(
                    status_code=400,
                    detail="Is required minimum one field")

            new_username = user_data.get('username', username)
            if new_username != username:
                username_constraint(new_username)
                if not libmongo.users.find_one({"username": new_username}):
                    zeta_data = libzeta.create_user(new_username)
                    user_data.update({'zeta': zeta_data})
                else:
                    raise HTTPException(
                        status_code=409,
                        detail=f"The username {new_username} already exists")
            else:
                if 'username' in user_data.keys():
                    del user_data['username']

            if user_data.get("zeta", False) and not user_data.get('username', False):
                zeta_data = libzeta.create_user(new_username)
                user_data.update({'zeta': zeta_data})

            libmongo.users.update_one(
                {"username": username},
                {"$set": user_data},
            )

            user_data = libmongo.users.find_one({"username": new_username})
            update_user = UserResponse.parse_obj(user_data)
        else:
            raise HTTPException(
                status_code=404,
                detail=f"The user with username {username} don't exists")
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return update_user

@app.get('/fake/users', response_model=FakeUserResponse)
def get_fake_users():
    count = 0
    try:
        fake = Faker()
        locations = [ fake.address() for i in range(0, 20)]
        users = []
        for i in range(0, 100):
            user = User(
                name=fake.name(),
                username=fake.unique.first_name(),
                location=locations[randrange(0, 20)],
            )
            user_data = user.dict()
            user_data.update({"zeta": libzeta.create_user(user.username)})
            users.append(user_data)
        result = libmongo.users.insert_many(users)
        count = len(result.inserted_ids)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return FakeUserResponse.parse_obj({"count": count})

@app.delete("/fake/users", response_model=FakeUserResponse)
def delete_fake_users():
    count = 0
    try:
        result = libmongo.users.delete_many({})
        count = result.deleted_count
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return FakeUserResponse.parse_obj({"count": count})

@app.get("/report/users")
def get_report_users():
    report = {}
    try:
        total = libmongo.users.count_documents({})
        if total == 0:
            raise HTTPException(
                status_code=404,
                detail="Not found records"
            )
        locations = libmongo.users.aggregate([{
            "$group": {
                "_id": "$location",
                "users": { "$sum": 1 }
            }
        }])
        for key, location in enumerate(locations):
            report.update({
                f"location_{key}": {
                    "location": location.get("_id"),
                    "users": location.get("users"),
                }})
        report.update({"_total": total})
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return report