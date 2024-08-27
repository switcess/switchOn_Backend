from pydantic import BaseModel

class VideoBase(BaseModel):
    date: str

class VideoResponseBase(BaseModel):
    date: str
    time: str
    actions: str