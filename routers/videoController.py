from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import domain.cctvEntity as cctvEntity
import schemas.videoFindAllRequest as videoFindAllRequest
import schemas.videoFindAllResponse as videoFindAllResponse
from database import SessionLocal, engine
from service import videoService
from typing import List

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
    prefix="/video", # 중복 URI 빼내기
    tags=["video"]
)

@router.post("/", response_model=List[videoFindAllResponse.VideoFindAllResponse])
def findAllVideo(request: videoFindAllRequest.VideoFindAllRequest, db: Session = Depends(get_db)):
    response = videoService.findAll_video(db=db, request=request)
    return response