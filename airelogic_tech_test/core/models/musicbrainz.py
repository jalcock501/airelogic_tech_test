""" MusicBrainz Request Model """
from typing import List, Optional
from pydantic import BaseModel, Field


class Artist(BaseModel):
    """ Artist BaseModel """
    id: str
    name: str
    disambiguation: Optional[str]


class Recording(BaseModel):
    """ Recording BaseModel """
    id: str
    title: str


class Release(BaseModel):
    """ Release BaseModel """
    id: str
    title: str


class Track(BaseModel):
    """ Track BaseModel """
    id: str
    title: str


class Tracklist(BaseModel):
    """ Track list BaseModel """
    tracks: Optional[List[Track]]


class MusicBrainzResponse(BaseModel):
    """ Response from MusicBrainz Request"""
    artists: Optional[List[Artist]]
    recordings: Optional[List[Recording]]
    releases: Optional[List[Release]]
    release_count: Optional[int] = Field(alias="release-count")
    media: Optional[List[Tracklist]]

    class Config:
        arbitrary_types_allowed = True
