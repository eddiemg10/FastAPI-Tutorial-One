from typing import List, Optional
from pydantic import BaseModel


class UserIn(BaseModel):
    name: str
    email: str
    password: str


class Blog(BaseModel):
    title: str
    body: str
    user_id: int

    class Config:
        orm_mode = True


class UserOut(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    author: UserOut

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
