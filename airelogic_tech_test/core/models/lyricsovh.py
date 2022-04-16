""" Models for LyricsOVH requests """

from pydantic import BaseModel


class LyricsResponse(BaseModel):
    lyrics: str
