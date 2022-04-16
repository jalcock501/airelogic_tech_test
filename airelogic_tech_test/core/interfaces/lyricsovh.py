""" 
Interface for the lyrics API:
https://lyricsovh.docs.apiary.io
"""


from core.tools.logger import Logger
from core.interfaces.apibase import ApiBaseClass
from core.models.lyricsovh import LyricsResponse

logger = Logger()


class LyricsAPI(ApiBaseClass):
    """ Api Class for the Lyrics API"""

    def get_lyrics(self, artist, song):
        """ Get lyrics for song based on song title and artist """
        query = f"{artist.name}/{song}"
        logger.info(f"request: {query}")
        self.resp = self.action(action=query, method="GET")
        logger.info(f"response: {self.resp.status_code}")
        return self.return_model(LyricsResponse)
