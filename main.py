from _controllers import user_controller
from _schemas import user_schema
from fastapi import FastAPI
import uvicorn


app = FastAPI(title = "Async FastAPI")


@app.post("/sign_up/")
async def sign_up(user: user_schema.UserSchema):
    res = await user_controller.sign_up(**user.dict())
    return res


if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)