from sqlalchemy.orm import Session
import domain.cctvEntity as cctvEntity, schemas.videoFindAllRequest as videoFindAllRequest
import domain.cctvEntity as cctvEntity, schemas.videoFindAllResponse as videoFindAllResponse

def findAll_video(db: Session, request: videoFindAllRequest.VideoFindAllRequest):
    videos = db.query(cctvEntity.CCTV).filter(cctvEntity.CCTV.date == request.date).all()
    
    videoList = [
        videoFindAllResponse.VideoFindAllResponse(
            id=video.id,
            date=video.date,
            time=video.time,
            actions=video.actions
        )
        for video in videos
    ]
    return videoList