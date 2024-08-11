from fastapi import FastAPI # type: ignore
from routers import healthCheck
from routers.cctv import cctvController
from pydantic import BaseModel
import schemas, models
from sqlalchemy.orm import Session

# from . import models, schemas

from routers.cctv import service
from database import SessionLocal, engine

app = FastAPI()
app.include_router(healthCheck.router)
app.include_router(cctvController.router)

