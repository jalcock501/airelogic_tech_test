""" Test LyricOVH API interface"""

from core.interfaces.lyricsovh import LyricsAPI
from core.tools.logger import Logger
from pydantic import BaseModel

logger = Logger(_file="tests.log", logging_level="debug")
test_lyrics = LyricsAPI(url="https://api.lyrics.ovh/v1/")


class MyTestArtist(BaseModel):
    id: str = "5b11f4ce-a62d-471e-81fc-a69a8278c7da"
    name: str = "Nirvana"
    disambiguation: str = "90s US grunge band"


lyrics = """Load up on guns, bring your friends\r\nIt's fun to lose and to pretend\r\nShe's overboard and self-assured\r\nOh no I know, a dirty word\r\nHello, hello, hello, how low\n\nHello, hello, hello, how low\n\nHello, hello, hello, how low\n\nHello, hello, hello\n\n\n\nWith the lights out it's less dangerous\n\nHere we are now, entertain us\n\nI feel stupid and contagious\n\nHere we are now, entertain us\n\nA mulatto, an Albino\n\nA mosquito, my libido, yeah\n\nHey, yay\n\n\n\nI'm worse at what I do best\n\nAnd for this gift, I feel blessed\n\nOur little group has always been\n\nAnd always will until the end\n\n\n\nHello, hello, hello, how low\n\nHello, hello, hello, how low\n\nHello, hello, hello, how low\n\nHello, hello, hello\n\n\n\nWith the lights out, it's less dangerous\n\nHere we are now, entertain us\n\nI feel stupid and contagious\n\nHere we are now, entertain us\n\nA mulatto, an Albino\n\nA mosquito, my libido, yeah\n\nHey, yay\n\n\n\n\n\nAnd I forget just why I taste\n\nOh yeah, I guess it makes me smile\n\nI found it hard, it was hard to find\n\nOh well, whatever, nevermind\n\n\n\nHello, hello, hello, how low\n\nHello, hello, hello, how low\n\nHello, hello, hello, how low\n\nHello, hello, hello\n\n\n\nWith the lights out, it's less dangerous\n\nHere we are now, entertain us\n\nI feel stupid and contagious\n\nHere we are now, entertain us\n\nA mulatto, an Albino\n\nA mosquito, my libido\n\n\n\nA denial, a denial, a denial, a denial, a denial\n\nA denial, a denial, a denial, a denial"""


def test_get_lyrics():
    artist = MyTestArtist()
    song = "Smells Like Teen Spirit"
    success, data = test_lyrics.get_lyrics(artist=artist, song=song)
    logger.info(f"{success}: {data}")
    assert success is True
    assert data.lyrics == lyrics
