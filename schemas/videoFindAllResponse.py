from .videoBaseSchemas import VideoResponseBase

class VideoFindAllResponse(VideoResponseBase):
    id: int
    date: str
    time: str
    actions: str