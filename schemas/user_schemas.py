from pydantic import BaseModel, Field, validator
import re


class UserSignUp(BaseModel):
    username: str = Field(...)
    password: str = Field(...)
    email: str = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)

    class Config:
        orm_mode = True

    @validator('username')
    def username_alphanumeric(cls, v):
        assert re.match("^[A-Za-z0-9_]*$", v), 'Username must contain alphabets, numbers and underscores only'
        #assert len(v) >= 5, 'Username must contain 5 characters or more'
        return v

    '''@validator('password')
    def username_valid(cls, v):
        assert len(v) >= 9, 'Password must contain 9 characters or more'
        return v'''

class UserSignIn(BaseModel):
    username: str = Field(...)
    password: str = Field(...)

    class Config:
        orm_mode = True

    @validator('username')
    def username_alphanumeric(cls, v):
        assert re.match("^[A-Za-z0-9_]*$", v), 'Username must contain alphabets, numbers and underscores only'
        return v

    '''@validator('password')
    def username_valid(cls, v):
        assert len(v) > 8, 'Password must contain 8 characters or more'
        return v'''

#print(UserSignIn.schema())

class DeleteUserSchema(BaseModel):
    password: str = Field(...)