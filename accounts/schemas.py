from ninja import Schema
from pydantic import EmailStr
from datetime import date 

class UserSchema(Schema):
    email: EmailStr
    name: str
    phone_number: str
    date_of_birth: date
    address: str
    gender: str
    profile_picture: str = None

class UserCreateSchema(UserSchema):
    password: str