from os import stat
from controllers.token_controllers import refresh_token, delete_token
from helpers import user_helpers
from models import user_model
from fastapi import status


async def sign_up(user):
    check = await user_model.get_user_by_username(user.username)
    if check != None:
        return status.HTTP_409_CONFLICT
    
    user.password = user_helpers.hash_password(user.password)
    res = await user_model.create_user(user)
    if res:
        return status.HTTP_200_OK
    
    return status.HTTP_400_BAD_REQUEST


async def sign_in(user):
    res = await user_model.get_user_by_username(user.username)
    if res:
        if user_helpers.check_password(user.password, res.password):
            token_value = await refresh_token(res.id)
            return token_value
    return False

async def sign_out(token_value):
    await delete_token(token_value)