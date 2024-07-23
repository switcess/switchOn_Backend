from typing import Union
from fastapi import FastAPI

# uvicorn HealthCheck:app --reload

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}