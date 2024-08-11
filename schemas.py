from typing import List, Union

from pydantic import BaseModel


# UserBase 생성
class CCTVBase(BaseModel):
    date: str
    time: str
    actions: str
    video: str


class CCTVCreate(CCTVBase):
    actions: str
    video: str


class CCTV(CCTVBase):
    id: int

    class Config:
        orm_mode = True