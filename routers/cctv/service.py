from sqlalchemy.orm import Session

# 기존에 생성한 모델과 스키마 불러오기
# from ... import models, schemas
import models, schemas


# 데이터 읽기 - ID로 사용자 불러오기
def get_cctv(db: Session, cctv_id: int):
    return db.query(models.CCTV).filter(models.CCTV.id == cctv_id).first()

# 데이터 생성하기
def create_cctv(db: Session, cctv: schemas.CCTVCreate):
    # SQLAlchemy 모델 인스턴스 만들기
    db_cctv = models.CCTV(date=cctv.date, time=cctv.time, actions=cctv.actions, video = cctv.video)
    db.add(db_cctv)  # DB에 해당 인스턴스 추가하기
    db.commit()  # DB의 변경 사항 저장하기
    db.refresh(db_cctv)  # 생성된 ID와 같은 DB의 새 데이터를 포함하도록 새로고침
    return db_cctv
