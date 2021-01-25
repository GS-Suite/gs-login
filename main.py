from controllers import user_controllers, token_controllers
from schemas.user_schema import UserSignIn, UserSignUp
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi import FastAPI, Response
from dotenv import load_dotenv
import uvicorn
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


app = FastAPI()


app.add_middleware(
    DBSessionMiddleware,
    db_url = os.environ["GS_DATABASE_URL"]
)


@app.post("/sign_up/")
async def sign_up(user: UserSignUp, response: Response):
    res, status = await user_controllers.sign_up(user)
    response.status_code = status
    return res

@app.post("/sign_in/")
async def sign_in(user: UserSignIn, response: Response):
    res, status =  await user_controllers.sign_in(user)
    response.status_code = status
    return res

@app.post("/validate_token/")
async def validate_token(token: str, response: Response):
    res, status = await token_controllers.validate_token(token)
    response.status_code = status
    return res


if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 8000)