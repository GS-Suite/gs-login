from pydantic import BaseModel, Json


class ClassroomSchema(BaseModel):
    id = int
    creator_id = int
    class_name = str
    # enrolled_users = Json

    class Config:
        orm_mode = True
