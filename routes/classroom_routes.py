from controllers import classroom_controllers, token_controllers
from fastapi import status


async def create_classroom(token, classroom):
    tkn, valToken_status_code = await token_controllers.validate_token(token)

    '''
        Be sure to notify the user on UI displaying user name
    '''

    if type(tkn) == dict and valToken_status_code == status.HTTP_200_OK:
        response = await classroom_controllers.create_class(token, classroom)
        if response == status.HTTP_200_OK:
            return {"success": True, "message": "Classroom created", "classroom_name": classroom.class_name}, response
        else:
            {"success": False, "message": "Classroom not created"}, response

    elif type(tkn) != dict and valToken_status_code == status.HTTP_200_OK:
        '''
            Here 'tkn' will be the refresh token
        '''
        response = await classroom_controllers.create_class(tkn, classroom)
        if response == status.HTTP_200_OK:
            return {"success": True, "message": "Classroom created", "classroom_name": classroom.class_name}, response
        else:
            {"success": False, "message": "Classroom not created"}, response

    else:
        return {"success": False, "message": "Non-existent user"}, status.HTTP_401_UNAUTHORIZED
