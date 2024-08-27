from pydantic import BaseModel
from .cctvBaseSchemas import CCTVBase

class CCTVCreate(CCTVBase):
    date: str
    time: str
    actions: str
    video: str