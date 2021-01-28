from pydantic import BaseModel, Json


class ClassroomSchema(BaseModel):
    class_name: str
    # enrolled_users = Json

    class Config:
        orm_mode = True
