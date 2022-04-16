""" Test Musicbrainz API interface"""

from core.interfaces.musicbrainz import MusicBrainz
from core.tools.logger import Logger
from pydantic import BaseModel

logger = Logger(_file="tests.log", logging_level="debug")
test_brainz = MusicBrainz(url="http://musicbrainz.org/ws/2/")


class MyTestArtist(BaseModel):
    id: str = "5b11f4ce-a62d-471e-81fc-a69a8278c7da"
    name: str = "Nirvana"
    disambiguation: str = "90s US grunge band"


class MyTestRelease(BaseModel):
    id: str = '0173cdb7-d43c-4497-8a2e-f0b0d27ac474'
    title: str = "Nevermind"


def test_get_artist():
    """ Test get artist returns with correct artist """
    artist = MyTestArtist()
    success, data = test_brainz.get_artist(artist=artist.name)
    logger.info(f"{success}: {data.artists}")
    assert success is True
    assert data.artists[0].id == artist.id
    assert data.artists[0].name == artist.name
    assert data.artists[0].disambiguation == artist.disambiguation


def test_get_release():
    """ Tests releases endpoint and functionality """
    artist = MyTestArtist()
    release = MyTestRelease()
    success, data = test_brainz.get_release_list(artist=artist)
    logger.info(f"{success}: {data.releases[0]}")
    assert success is True
    assert data.releases[0].id == release.id
    assert data.releases[0].title == release.title


def test_get_song_list():
    """ Tests Recordings Endpoint and Functionality """
    release = MyTestRelease()
    success, data = test_brainz.get_song_list(release=release)
    logger.info(f"{success}: {data.media[0]}")
    assert success is True
    assert data.media[0].tracks[0].id == '7a513f39-11ea-4332-9294-157f60255113'
    assert data.media[0].tracks[0].title == 'Smells Like Teen Spirit'
