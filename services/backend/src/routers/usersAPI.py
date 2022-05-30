from fastapi import APIRouter, Body, HTTPException, status,Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from src.auth.auth_handler import signJWT
from src.auth.auth_bearer import JWTBearer
import datetime


from typing import  List

from src.users.users import UsersModel,UpdateUsersModel,UserLoginModel,get_password_hash,verify_password
from ..settings import mongoData

from decouple import config

router = APIRouter()


# Auth
# ======================================================================================================

# create one user data
@router.post("/signup", response_description="Add new user", response_model=UsersModel, tags=["auth"])
async def create_new_User(user: UsersModel = Body(...)):
    if (existing_user := await mongoData["users"].find_one({"email": user.email})) is not None:
        raise HTTPException(status_code=400, detail="Email Duplicated")
    # transfer user password into hash format
    user.password = get_password_hash(user.password)

    user = jsonable_encoder(user)
    new_user = await mongoData["users"].insert_one(user)
    created_user = await mongoData["users"].find_one({"_id": new_user.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)

#  user login
@router.post("/login", tags=["auth"])
async def user_login(loginUser: UserLoginModel = Body(...)):
    # return loginUser.email
    user = await mongoData["users"].find_one({"email": loginUser.email})
    if user is not None :
        if verify_password(loginUser.password,user["password"]):
            return signJWT(user["email"])
        raise HTTPException(status_code=400, detail="Password Error")

    raise HTTPException(status_code=404, detail="Account Not Found")

# =====================================================================================================

# get all users
@router.get("/users", response_description="List all users", response_model=List[UsersModel], tags=["users"], dependencies=[Depends(JWTBearer())])
async def get_all_Users():
    users = await mongoData["users"].find().to_list(1000)
    return users

# get one of the users
@router.get("/users/{id}", response_description="Get a single user", response_model=UsersModel, tags=["users"], dependencies=[Depends(JWTBearer())])
async def show_User(id: str):
    if (user := await mongoData["users"].find_one({"_id": id})) is not None:
        return user

    raise HTTPException(status_code=404, detail=f"user {id} not found")




# update one user data
@router.put("/users/{id}", response_description="Update a user", response_model=UsersModel, tags=["users"], dependencies=[Depends(JWTBearer())])
async def update_user(id: str, user: UpdateUsersModel = Body(...)):
    user = {k: v for k, v in user.dict().items() if v is not None}
    
    if len(user) >= 1:
        
        # user["password"] = get_password_hash(user["password"])
        print("user",user)
        update_result = await mongoData["users"].update_one({"_id": id}, {"$set": user})

        if update_result.modified_count == 1:
            if (
                updated_user := await mongoData["users"].find_one({"_id": id})
            ) is not None:
                return updated_user

    if (existing_user := await mongoData["users"].find_one({"_id": id})) is not None:
        return existing_user

    raise HTTPException(status_code=404, detail=f"user {id} not found")

# delete one user data
@router.delete("/users/{id}", response_description="Delete a user", tags=["users"], dependencies=[Depends(JWTBearer())])
async def delete_user(id: str):
    delete_result = await mongoData["users"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=200, content="delete success")

    raise HTTPException(status_code=404, detail=f"user {id} not found")