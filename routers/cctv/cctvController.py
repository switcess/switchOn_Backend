from fastapi import APIRouter, Depends # type: ignore
from sqlalchemy.orm import Session
import schemas, models
from database import SessionLocal, engine
from routers.cctv import service

#DB 테이블 생성
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix="/cctv",
    tags=["cctv"]
)

@router.post("/", response_model=schemas.CCTV)
def create_cctv(cctv: schemas.CCTVCreate, db: Session = Depends(get_db)):
    return service.create_cctv(db=db, cctv=cctv)