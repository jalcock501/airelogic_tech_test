''' MAIN '''
from textwrap import shorten
from unicodedata import name
import typer

from core.tools.logger import Logger
from core.tools.lyricsovh import find_lyrics
from core.tools.musicbrainz import find_artist, find_song_list

app = typer.Typer()
logger = Logger()


@app.command()
def main(artist: str = typer.Argument("Nirvana", help="Name of the Artist you wish to search for")):
    """ 
    CLI program to find mean number of words 
    the whole collection of an Artists songs 
    """
    # Find artist in MusicBrainz API
    found_artist = find_artist(artist)
    songs = find_song_list(found_artist=found_artist)
    lyrics = find_lyrics(found_artist=found_artist, songs=songs)


if __name__ == '__main__':
    app()
