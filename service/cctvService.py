from sqlalchemy.orm import Session # type: ignore

# 기존에 생성한 모델과 스키마 불러오기
# from ... import models, schemas
import domain.cctvEntity as cctvEntity, schemas.cctvCreateRequest as cctvCreateRequest


# 데이터 읽기 - ID로 사용자 불러오기
def get_cctv(db: Session, cctv_id: int):
    return db.query(cctvEntity.CCTV).filter(cctvEntity.CCTV.id == cctv_id).first()

# 데이터 생성하기
def create_cctv(db: Session, cctv: cctvCreateRequest.CCTVCreate):
    # SQLAlchemy 모델 인스턴스 만들기
    db_cctv = cctvEntity.CCTV(date=cctv.date, time=cctv.time, actions=cctv.actions, video = cctv.video)
    db.add(db_cctv)  # DB에 해당 인스턴스 추가하기
    db.commit()  # DB의 변경 사항 저장하기
    db.refresh(db_cctv)  # 생성된 ID와 같은 DB의 새 데이터를 포함하도록 새로고침
    return db_cctv

def delete_cctv(db: Session, cctv_id: int):
    db_cctv = db.query(cctvEntity.CCTV).filter(cctvEntity.CCTV.id == cctv_id).first()
    if db_cctv: #데이터 존재하는 경우
        db.delete(db_cctv)  # CCTV 항목 삭제하기
        db.commit()  # DB의 변경 사항 저장하기
        return {"message": "CCTV item deleted"}
    else:
        return {"message": "CCTV item not found"}