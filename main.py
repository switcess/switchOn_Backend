from fastapi import FastAPI # type: ignore

# def create_app() -> FastAPI:
#     _app = FastAPI()
#     _app.include_router()

#     return _app

# app = create_app()


app = FastAPI()

from routers import healthCheck
app.include_router(healthCheck.router)