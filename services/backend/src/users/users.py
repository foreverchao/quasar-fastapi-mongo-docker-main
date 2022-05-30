from sqlite3 import Timestamp
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional
import datetime
from passlib.context import CryptContext

from src.common.common import PyObjectId





# user password into hash password
# =========================================================
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# check whether login password is same as hash password 
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# when user create new account, transfer password into hash password
def get_password_hash(password):
    return pwd_context.hash(password)



# user model
# =========================================================

class UserLoginModel(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "root@test.com",
                "password": "123"
            }
        }

class UsersModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    role:list = Field(...)
    createdAt: str = datetime.datetime.now()
    updatedAt: str = datetime.datetime.now()


    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Root",
                "email": "root@test.com",
                "password": "123",
                "role":["Admin"],
                
            }
        }


class UpdateUsersModel(BaseModel):
    name: str = Field(...)
    email: Optional[EmailStr]
    role:list = Field(...)
    updatedAt: str = Field(...)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Root",
                "role":["Admin"],
                "updatedAt":""
            }
        }