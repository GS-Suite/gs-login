from fastapi import FastAPI, Response, BackgroundTasks, Header, Body
from controllers import user_controllers, token_controllers
from schemas.user_schemas import UserSignIn, UserSignUp, DeleteSchema
from schemas.classroom_schemas import ClassroomSchema
from fastapi_sqlalchemy import DBSessionMiddleware
from routes import user_routes, classroom_routes
from dotenv import load_dotenv
from typing import Optional
import uvicorn
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


app = FastAPI()


app.add_middleware(
    DBSessionMiddleware,
    db_url=os.environ["GS_DATABASE_URL"]
)


@app.post("/sign_up/")
async def sign_up(user: UserSignUp, response: Response):
    return await user_routes.sign_up(user, response)


@app.post("/sign_in/")
async def sign_in(user: UserSignIn, response: Response):
    return await user_routes.sign_in(user, response)


@app.post("/sign_out/")
async def sign_out(token: str, response: Response, background_tasks: BackgroundTasks):
    return await user_routes.sign_out(token, response, background_tasks)


@app.post("/validate_token/")
async def validate_token(token: str, response: Response):
    res, status = await token_controllers.validate_token(token)
    response.status_code = status
    return res


@app.post("/create_classroom/")
async def create_classroom(token: str, classroom: ClassroomSchema):
    return await classroom_routes.create_classroom(token, classroom)


@app.post("/delete_account/")
async def delete_account(response: Response, password: DeleteSchema, token: str = Header(None)):
    return await user_routes.delete_account(password, token, response)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
