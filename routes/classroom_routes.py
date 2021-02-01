from controllers import classroom_controllers, token_controllers
from fastapi import status


async def create_classroom(token, classroom):
    token_response = await token_controllers.validate_token(token)

    '''
        Be sure to notify the user on UI displaying user name
    '''
    #print(token_response)

    if token_response:
        response = await classroom_controllers.create_class(token, classroom)
        if response == status.HTTP_200_OK:
            return {"success": True, "message": "Classroom created", "classroom_name": classroom.class_name}, response
        else:
            {"success": False, "message": "Classroom not created"}, response
    else:
        return {"success": False, "message": "Non-existent user"}, status.HTTP_401_UNAUTHORIZED