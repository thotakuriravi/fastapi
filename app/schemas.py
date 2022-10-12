



from typing import Optional
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime

class Post(BaseModel):
    title: str
    content:str
    published: bool = True


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    id:int
    title:str
    content:str
    published:bool
    created_at: datetime
    owner_id: int
    owner: UserOut
    class Config:
        orm_mode = True

class PostOut_Vote(BaseModel):
    Post: PostOut
    votes: int

    class Config:
        orm_mode = True


class User(BaseModel):
    email: EmailStr
    password: str



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


class Vote(BaseModel):
    post_id:int
    dir: conint(le=1)

