from models import user_model
import bcrypt


def hash_password(password):
    return bcrypt.hashpw(
        password.encode("utf-8"), 
        bcrypt.gensalt()
    ).decode("utf-8")

def check_password(password, hashed):
    print(password.encode("utf-8"))
    print(hashed.encode("utf-8"))
    return bcrypt.checkpw(
        password.encode("utf-8"), 
        hashed.encode("utf-8")
    )


async def sign_up(user):
    ### processing
    user.password = hash_password(user.password)
    res = await user_model.create_user(user)
    return res


async def sign_in(user):
    res = await user_model.get_user_by_username(user.username)
    if res:
        return check_password(user.password, res.password)
    return False