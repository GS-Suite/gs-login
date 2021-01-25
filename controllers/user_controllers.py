from controllers.token_controllers import refresh_token, delete_token
from helpers import user_helpers
from models import user_model
from fastapi import status


async def sign_up(user):
    check = await user_model.get_user_by_username(user.username)
    if check != None:
        return {
            "success": False,
            "message": "An account with that username already exists"
        }, status.HTTP_409_CONFLICT
    else:            
        user.password = user_helpers.hash_password(user.password)
        res = await user_model.create_user(user)
        if res:
            return {
                "success": True,
                "message": "Your account has been created",
            }, status.HTTP_201_CREATED
        else:
            return {
                "success": False,
                "message": "Account not created",
            }, status.HTTP_400_BAD_REQUEST


async def sign_in(user):
    res = await user_model.get_user_by_username(user.username)
    if res:
        if user_helpers.check_password(user.password, res.password):
            return {
                "success": True,
                "message": "Successfully logged in",
                "data": {
                    "token": await refresh_token(res.id)
                }
            }, status.HTTP_200_OK
    return {
        "success": False,
        "message": "Invalid username or password"
    }, status.HTTP_401_UNAUTHORIZED

async def sign_out(token_value):
    res = await delete_token(token_value)
    #print(res)
    if res:    
        return {
            "success": True,
            "message": "Successfully logged out"
        }, status.HTTP_200_OK
    return {
            "success": False,
            "message": "Invalid token"
        }, status.HTTP_401_UNAUTHORIZED