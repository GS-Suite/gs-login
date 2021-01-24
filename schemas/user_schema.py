from pydantic import BaseModel


class UserSignUp(BaseModel):
    username: str
    password: str
    email: str
    first_name: str
    last_name: str

    class Config:
        orm_mode = True

class UserSignIn(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True