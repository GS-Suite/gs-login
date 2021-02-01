from models import classroom_model
from controllers.token_controllers import get_token_by_value
from fastapi import status


async def create_class(token, classroom):
    # GET USER FROM TOKEN, PASS user id while creating class

    res = await get_token_by_value(token)
    # print(res.user_id)
    # print(type(classroom.class_name))

    resp = await classroom_model.create_classroom(res.user_id, classroom)
    # print(resp)
    if resp == True:
        return status.HTTP_200_OK
    else:
        return status.HTTP_400_BAD_REQUEST
