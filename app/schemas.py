



from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class Post(BaseModel):
    title: str
    content:str
    published: bool = True

class PostOut(BaseModel):
    id:int
    title:str
    content:str
    published:bool
    created_at: datetime
    class Config:
        orm_mode = True


class User(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email:EmailStr
    password:str

class TokenData(BaseModel):
    id: Optional[str] = None

class TokenOut(BaseModel):
    access_token:str
    token_type:str

    class Config:
        orm_mode = True