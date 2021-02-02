from controllers import classroom_controllers, token_controllers
from fastapi import status


async def create_classroom(token, classroom):
    tkn_validation_resp = await token_controllers.validate_token(token)

    if tkn_validation_resp != False:
        tkn = tkn_validation_resp['token']
        #print(tkn)
        response = await classroom_controllers.create_class(tkn, classroom)
        if response == status.HTTP_200_OK:
            return {"success": True, "message": "Classroom created", "classroom_name": classroom.class_name}, response
        else:
            return {"success": False, "message": "Classroom not created"}, response
    else:
        return {"success": False, "message": "Non-existent user"}, status.HTTP_401_UNAUTHORIZED