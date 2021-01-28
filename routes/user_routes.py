from os import stat
from controllers import user_controllers, token_controllers
from fastapi import status


async def sign_up(user, response):
    stts = await user_controllers.sign_up(user)
    response.status_code = stts
    if stts == 200:
        return {
            "success": True,
            "message": "Your account has been created"
        }
    elif stts == 409:
        return {
            "success": False,
            "message": "An account with that username already exists"
        }
    else:
        return {
            "success": False,
            "message": "Account not created"
        }

async def sign_in(user, response):
    res = await user_controllers.sign_in(user)
    if res:
        response.status_code = status.HTTP_200_OK
        return {"success": True, "message": "Successfully logged in", "data": {"token": res}}

    response.status_code = status.HTTP_401_UNAUTHORIZED
    return {"success": False, "message": "Invalid username or password"}

async def sign_out(token, response, background_tasks):
    background_tasks.add_task(user_controllers.sign_out, token_value = token)
    response.status_code = 200
    return {"success": True, "message": "Successfully logged out"}