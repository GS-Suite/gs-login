from models import classroom_model
from fastapi import status


async def create_class(classroom, token):
    ### GET USER FROM TOKEN, PASS user id while creating class

    user_id = None

    res = await classroom_model.create_classroom(classroom, user_id)
    if res == True:
        return status.HTTP_200_OK
    else:
        return status.HTTP_400_BAD_REQUEST
