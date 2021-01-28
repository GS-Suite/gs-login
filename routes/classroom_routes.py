from controllers import classroom_controllers, token_controllers
from fastapi import status


async def create_classroom(token, classroom, response):
    res, stat = await token_controllers.validate_token(token)
    if stat == status.HTTP_200_OK:
        stat = await classroom_controllers.create_class(classroom, token)
        response.status_code = stat
        if stat == 400:
            return {
                "success": False,
                "message": "Non-existent user"
            } 
        elif stat == 200:
            return {
                "success": True,
                "message": "Classroom created",
                "classroom_name": classroom.class_name
            }
        else:
            return {
                "success": False,
                "message": "Classroom not created",
            }, 
    else:
        response.status_code = stat
        return {
            "success": False,
            "message":  "Invalid token"
        }