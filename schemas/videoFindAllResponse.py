from .videoBaseSchemas import VideoResponseBase

class VideoFindAllResponse(VideoResponseBase):
    date: str
    time: str
    actions: str