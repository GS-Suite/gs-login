from models import token_model


async def validate_token(token):
    ### processing
    res = await token_model.get_token_by_value(token)
    print(res)
    return res