from pydantic import BaseModel


class Message(BaseModel):
    message: str


class User(BaseModel):
    id: int
    name: str
    email: str
    age: int
    is_admin: bool
