from pydantic import BaseModel
from typing import Optional, List

class Zeta(BaseModel):
    username: str
    token: str
    profiles: List[str] = []

class User(BaseModel):
    name: str
    username: str
    location: str
    
class UserResponse(User):
    zeta: Zeta

class UserUpdate(BaseModel):
    name: Optional[str]
    username: Optional[str]
    location: Optional[str]
    zeta: Optional[bool]

class DeleteResponse(BaseModel):
    deleted: bool

class FakeUserResponse(BaseModel):
    count: int
    