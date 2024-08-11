from fastapi import FastAPI, Depends, Path, HTTPException # type: ignore
from routers import healthCheck
from pydantic import BaseModel
import schemas, models
from sqlalchemy.orm import Session

# from . import models, schemas

from routers.cctv import service
from database import SessionLocal, engine

app = FastAPI()

#DB 테이블 생성
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(healthCheck.router)


@app.post("/cctv", response_model=schemas.CCTV)
def create_cctv(cctv: schemas.CCTVCreate, db: Session = Depends(get_db)):
    return service.create_cctv(db=db, cctv=cctv)