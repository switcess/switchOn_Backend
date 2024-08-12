from fastapi import APIRouter, Depends # type: ignore
from sqlalchemy.orm import Session # type: ignore
import schemas.cctvCreateRequest as cctvCreateRequest, domain.cctvEntity as cctvEntity
import schemas.cctvBaseSchemas as cctvBaseSchemas

from database import SessionLocal, engine
from service import cctvService

#DB 테이블 생성
cctvEntity.Base.metadata.create_all(bind=engine)

# DB 커넥팅
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix="/cctv", # 중복 URI 빼내기
    tags=["cctv"]
)

@router.post("/", response_model=cctvBaseSchemas.CCTV) # prefix 있어서 /cctv API로 요청 보내야 함.
def create_cctv(cctv: cctvCreateRequest.CCTVCreate, db: Session = Depends(get_db)):
    return cctvService.create_cctv(db=db, cctv=cctv)