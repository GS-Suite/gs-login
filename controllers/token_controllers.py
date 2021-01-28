from sqlalchemy.sql.elements import False_
from models import token_model
from helpers import token_helpers
from dotenv import load_dotenv
from fastapi import status
import datetime
import os


BASE_DIR = os.path.dirname(os.path.abspath("gs-login"))
load_dotenv(os.path.join(BASE_DIR, ".env"))

TOKEN_VALIDITY = datetime.timedelta(seconds = int(os.environ["TOKEN_VALIDITY"]))


async def validate_token(token):
    ### processing
    res = await token_model.get_token_by_value(token)
    if res:
        time_left = res.date_issued - datetime.datetime.now() + TOKEN_VALIDITY
        if time_left > datetime.timedelta(seconds=0):
            return {
                "success": True,
                "message": "Valid token",
                "data": {
                    "token": res.token_value,
                    "valid_for": time_left 
                }
            }, status.HTTP_200_OK
        else:
            return await refresh_token(res.user_id)
    else:
        return {
            "success": False,
            "message": "Invalid token"
        }, status.HTTP_401_UNAUTHORIZED


async def create_token(user_id):
    token_value = await token_helpers.generate_token()
    token = await token_model.create_token(user_id, token_value)
    if token:
        return {
            "token": token.token_value,
            "issued_at": token.date_issued
        }
    return {
        "token": None
    }


async def refresh_token(user_id):
    token_value = await token_helpers.generate_token()
    token = await token_model.get_token_by_user(user_id)
    print("token", token)
    if token:
        refreshed = await token_model.update_token(token, token_value)
        if refreshed:
            return {
                "token": refreshed.token_value,
                "issued_at": refreshed.date_issued
            }
    else:
        return await create_token(user_id)


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