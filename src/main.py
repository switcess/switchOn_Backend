from fastapi import FastAPI
from routers.user_router import user

def create_app() -> FastAPI:
    _app = FastAPI()
    _app.include_router(user)

    return _app

app = create_app()