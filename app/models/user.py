from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: Optional[str] = None
    fullname: Optional[str] = None
    disabled: Optional[bool] = None


class User(UserBase):
    hashed_password: str
