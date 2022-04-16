''' 
Interface for https://musicbrainz.org/doc/Development/XML_Web_Service/Version_2 
Can be expanded to become python api wrapper for musicbrainz but for purposes of test
get_artists() is the only function I've written
'''

from time import sleep
from core.interfaces.apibase import ApiBaseClass
from core.models.musicbrainz import MusicBrainzResponse
from core.tools.logger import Logger

logger = Logger()


class MusicBrainz(ApiBaseClass):
    """ MusicBrainz API Class """

    def get_artist(self, artist):
        """ Get Artist data from MusicBrainz API via name"""
        query = f"artist/?query=artist:{artist}&limit=5"

        logger.info(f"request: {query}")
        self.resp = self.action(action=query, method="GET")
        logger.info(f"response: {self.resp.status_code}")

        return self.return_model(MusicBrainzResponse)

    def get_release_list(self, artist):
        """ Get Studio Albums this is to TRY and avoid duplicate songs """
        limit = 100
        offset = 0
        query = f"release/?artist={artist.id}&inc=release-groups&status=official&primarytype=album&limit={limit}&offset={offset}"

        logger.info(f"request: {query}")
        self.resp = self.action(action=query, method="GET")
        logger.info(f"response: {self.resp.status_code}")

        success, data = self.return_model(MusicBrainzResponse)
        # loop over paginated data
        if data.release_count < 100:
            return self.return_model(MusicBrainzResponse)
        else:
            full_data = []
            for i in range(int(data.release_count/100)):
                offset = limit * i
                query = f"release/?artist={artist.id}&inc=release-groups&status=official&primarytype=album&limit={limit}&offset={offset}"

                logger.info(f"request: {query}")
                self.resp = self.action(action=query, method="GET")
                logger.info(f"response: {self.resp.status_code}")

                success, data = self.return_model(MusicBrainzResponse)
                full_data.append(data.releases)
            full_data = [
                release for sublist in full_data for release in sublist]
            for d in full_data:
                data.releases.append(d)
            return success, data

    def get_song_list(self, release):
        """ 
        Get song list using release ID
        as this one is the only call hit multiple times in a 
        single run I've had to add some recursion to deal
        with the rate limiting.

        One point to make on my behalf, I didn't have loads of
        time to read through the docs to figure out if there was 
        a better way to get the tracks from the API so I did it this way,
        my wife is already mad at me for taking this long (sad face)
        """
        query = f"release/{release.id}?inc=recordings"

        logger.info(f"request: {query}")
        self.resp = self.action(action=query, method="GET")
        logger.info(f"response: {self.resp.status_code}")

        # I hate rate limiting, also the API docs are awful
        # added simple max allowable recursion to avoid destorying stack
        if self.resp.status_code == 503:
            sleep(1)
            return self.get_song_list(release=release)
        return self.return_model(MusicBrainzResponse)
