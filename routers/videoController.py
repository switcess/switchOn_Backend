from fastapi import APIRouter, Depends # type: ignore
from sqlalchemy.orm import Session # type: ignore
import schemas.cctvCreateRequest as cctvCreateRequest, domain.cctvEntity as cctvEntity
import schemas.videoFindAllRequest as videoFindAllRequest
import schemas.videoFindAllResponse as videoFindAllResponse
from database import SessionLocal, engine
from service import videoService

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

@router.post("/", response_model=videoFindAllResponse.VideoFindAllResponse)
# @router.post("/")
def findAllVideo(request: videoFindAllRequest.VideoFindAllRequest, db: Session = Depends(get_db)):
    response = videoService.findAll_video(db=db, request=request)
    if response is None:
        return {"detail": "해당 날짜에 비디오가 존재하지 않습니다."}
    return response
    # return "돼라."