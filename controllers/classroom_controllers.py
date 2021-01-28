from models import classroom_model
from fastapi import status


async def create_class(classroom):
    res = await classroom_model.create_classroom(classroom)
    if res == None:
        return {
            "message": "Non-existent user"
        }
    if res == True:
        return {
            "message": "Classroom created",
            "classroom_name": classroom.name
        }, status.HTTP_200_OK
    else:
        return {
            "message": "Classroom not created",
        }, status.HTTP_400_BAD_REQUEST
