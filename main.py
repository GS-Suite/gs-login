from schemas import user_schemas, token_schemas, classroom_schemas
from routes import user_routes, classroom_routes, token_routes
from fastapi import FastAPI, Response, BackgroundTasks, Header
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
import uvicorn
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()

app.add_middleware(
    DBSessionMiddleware,
    db_url=os.environ["GS_DATABASE_URL"]
)

origins = [
    "http://localhost:3000",
    "https://gstestreact.herokuapp.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home_to_doc():
    return RedirectResponse("/docs")

'''USER APIS'''


@app.post("/sign_up/")
async def sign_up(user: user_schemas.UserSignUp, response: Response):
    return await user_routes.sign_up(user, response)


@app.post("/sign_in/")
async def sign_in(user: user_schemas.UserSignIn, response: Response):
    return await user_routes.sign_in(user, response)


@app.post("/sign_out/")
async def sign_out(token: str, response: Response, background_tasks: BackgroundTasks):
    return await user_routes.sign_out(token, response, background_tasks)


@app.post("/delete_account/")
async def delete_account(response: Response, password: user_schemas.DeleteUserSchema, token: str = Header(None)):
    return await user_routes.delete_account(password, token, response)


'''TOKEN APIS'''


@app.post("/validate_token/")
async def validate_token(token: token_schemas.TokenValidate, response: Response):
    return await token_routes.validate_token(token, response)


@app.post("/refresh_token/")
async def refresh_token(token: token_schemas.TokenValidate, response: Response):
    return await token_routes.refresh_token(token, response)


'''CLASSROOM APIS'''


@app.post("/create_classroom/")
async def create_classroom(classroom: classroom_schemas.ClassroomSchema, token: str = Header(None)):
    return await classroom_routes.create_classroom(token, classroom)
