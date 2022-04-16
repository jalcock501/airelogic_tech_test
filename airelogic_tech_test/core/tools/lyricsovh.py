""" functions for handling Lyrics data """

import typer
import unicodedata
from statistics import mean
from core.interfaces.cli import style
from core.interfaces.lyricsovh import LyricsAPI


lyrics_api = LyricsAPI(url="https://api.lyrics.ovh/v1/")


def find_lyrics(found_artist, songs):
    """ get lyrics from api.lyrcis.ovh """
    total = 1000
    song_length_list = []
    with typer.progressbar(length=total, label=style(typer.colors.GREEN, "Getting Lyrics")) as progress:
        for song in songs:
            success, resp = lyrics_api.get_lyrics(
                artist=found_artist, song=song)
            progress.update(total/len(songs))
            if success:
                song_length = len(resp.lyrics.split())
                song_length_list.append(song_length)

    # this looks alot but it's just a bunch of transmutes from list to mean float to rounded int to string
    typer.echo(f"Average (Mean) number of words in a {style(typer.colors.RED, found_artist.name.upper())} song is:\
     {style(typer.colors.BRIGHT_GREEN,str(round(mean(song_length_list))))}")
