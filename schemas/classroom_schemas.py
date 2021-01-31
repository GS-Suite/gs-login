from pydantic import BaseModel, Json


class ClassroomSchema(BaseModel):
    class_name: str

    class Config:
        orm_mode = True
