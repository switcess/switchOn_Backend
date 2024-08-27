from pydantic import BaseModel # type: ignore


# CCTVBase 생성
class CCTVBase(BaseModel):
    date: str
    time: str
    actions: str
    video: str

class CCTV(CCTVBase):
    id: int

    class Config:
        orm_mode = True