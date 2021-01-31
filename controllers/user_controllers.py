from controllers import token_controllers
from helpers import user_helpers
from models import user_model
from fastapi import status


async def sign_up(user):
    check = await user_model.get_user_by_username(user.username)
    if check == None:    
        user.password = user_helpers.hash_password(user.password)
        res = await user_model.create_user(user)
        if res:
            return status.HTTP_200_OK
        else:
            return status.HTTP_400_BAD_REQUEST
    return status.HTTP_409_CONFLICT


async def sign_in(user):
    ''' get user '''
    res = await user_model.get_user_by_username(user.username)
    if res:
        ''' check password '''
        if user_helpers.check_password(user.password, res.password):
            token_value = await token_controllers.refresh_token(res.id)
            return token_value
    return False


async def sign_out(token_value):
    await token_controllers.delete_token(token_value)


async def delete_account(password, token):
    token = await token_controllers.get_token_by_value(token)
    if token == None:
        return status.HTTP_401_UNAUTHORIZED
    try:
        '''get user'''
        user = await user_model.get_user_by_id(token.user_id)
        if user == None:
            return status.HTTP_401_UNAUTHORIZED
        
        '''check password'''
        if not user_helpers.check_password(password, user.password):
            return status.HTTP_401_UNAUTHORIZED

        '''delete tokens'''
        await token_controllers.delete_user_tokens(user.id)

        ''' delete other data'''
        
        '''delete user'''
        await user_model.delete_user(user)
        return status.HTTP_200_OK
    
    except Exception as e:
        print(e)
        return status.HTTP_400_BAD_REQUEST

