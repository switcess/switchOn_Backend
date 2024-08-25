from sqlalchemy.orm import Session
from fastapi import HTTPException

# 기존에 생성한 모델과 스키마 불러오기
# from ... import models, schemas
import domain.cctvEntity as cctvEntity, schemas.videoFindAllRequest as videoFindAllRequest
import domain.cctvEntity as cctvEntity, schemas.videoFindAllResponse as videoFindAllResponse

from datetime import datetime

def findAll_video(db: Session, request: videoFindAllRequest.VideoFindAllRequest):
    video = db.query(cctvEntity.CCTV).filter(cctvEntity.CCTV.date == request.date).first()
    
    if not video:
        raise HTTPException(status_code=404, detail="CCTV item not found")
    
    videoResponse = videoFindAllResponse.VideoFindAllResponse(
            date=video.date,
            time=video.time,
            actions=video.actions
        )
    
    return videoResponse
