from models import user_model


async def sign_up(user):
    ### processing
    res = await user_model.create_user(user)
    return res


async def sign_in(user):
    ### processing
    res = await user_model.login(user)
    return res