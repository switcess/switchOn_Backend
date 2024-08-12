from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# database.py에서 생성한 Base import
from database import Base


# Base를 상속 받아 SQLAlchemy model 생성
class CCTV(Base):
    # 해당 모델이 사용할 table 이름 지정
    __tablename__ = "cctv"

    # Model의 attribute(column) 생성 -> "="를 사용하여 속성을 정의
    id = Column(Integer, primary_key=True, index=True)
    date = Column(String(100), index=True) # 날짜로 바꿔야 함.
    time = Column(String(100), index=True)
    actions = Column(String(100), index=True)
    video = Column(String(100), index=True)