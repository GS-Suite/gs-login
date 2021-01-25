from models import token_model
from helpers import token_helpers

async def validate_token(token):
    ### processing
    res = await token_model.get_token_by_value(token)
    #print(res)
    return res

async def refresh_token(user):
    token_value = await token_helpers.generate_token()
    token = await token_model.get_token_by_user(user)
    print("token", token)
    if token:
        refreshed = await token_model.update_token(token, token_value)
        if refreshed:
            return {
                "token_value": refreshed.token_value,
                "issued_at": refreshed.date_issued
            }
    else:
        return await create_token(user)

async def create_token(user):
    token_value = await token_helpers.generate_token()
    token = await token_model.create_token(user, token_value)
    if token:
        return {
            "token_value": token.token_value,
            "issued_at": token.date_issued
        }
    return False

async def delete_token(token_value):
    token = token_model.get_token_by_value(token_value)
    if token:
        return token_model.delete_token(token)