from helpers import token_helpers
from models import token_model
import constants
import datetime


TOKEN_VALIDITY = datetime.timedelta(seconds=int(constants.TOKEN_VALIDITY))
REFRESH_TIMEOUT = datetime.timedelta(seconds=int(constants.REFRESH_TIMEOUT))


async def validate_token(token):
    # processing
    res = await token_model.get_token_by_value(token)
    # print(res)
    if res:
        time_left = res.date_issued - datetime.datetime.now() + TOKEN_VALIDITY
        if time_left < datetime.timedelta(seconds=0):
            return False
        elif time_left < REFRESH_TIMEOUT:
            return await refresh_token(res.user_id)
        else:
            return {
                "token": res.token_value,
                "valid_for": time_left
            }
    else:
        return False


async def refresh_token(user_id):
    # print("refreshing")
    token_value = await token_helpers.generate_token()
    res = await token_model.refresh_token(user_id, token_value)
    # print(res.user_id)
    if res:
        return {
            "token": res.token_value,
            "valid_for": res.date_issued - datetime.datetime.now() + TOKEN_VALIDITY
        }
    return False


async def refresh_token_by_token(token_value):
    token = await get_token_by_value(token_value)
    if token:
        res = await refresh_token(token.user_id)
        if res:
            return res
    return False


async def get_token_by_value(token_value):
    return await token_model.get_token_by_value(token_value)


async def delete_user_tokens(user_id):
    tokens = await token_model.get_token_by_user(user_id)
    await token_model.delete_token(tokens)


async def delete_token(token_value):
    token = await token_model.get_token_by_value(token_value)
    if token:
        return await token_model.delete_token(token)
    return True
