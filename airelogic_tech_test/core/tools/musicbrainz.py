""" Functions for handling MusicBrainz data """
from time import sleep
import typer
from core.interfaces.cli import style
# local imports
from core.models.musicbrainz import MusicBrainzResponse
from core.interfaces.musicbrainz import MusicBrainz

# musicbrainz api handler
musicbrainz = MusicBrainz(url="http://musicbrainz.org/ws/2/")


def find_artist(search_artist):
    """ Search MusicBrainz and find artist(s) with search name"""
    typer.echo(f"Searching for {search_artist}")
    success, data = musicbrainz.get_artist(search_artist)
    if success:
        if len(data.artists) > 1:
            # if multiple artists with similiar names give user option to pick correct one
            typer.echo(
                f"There are multiple Artists with the name: {style(typer.colors.RED, search_artist.upper())}")
            for idx, artist in enumerate(data.artists):
                if not artist.disambiguation:
                    typer.echo(
                        f"{style(typer.colors.BLUE, idx)}: {artist.name}")
                else:
                    typer.echo(
                        f"{style(typer.colors.BLUE, idx)}: {artist.name} the {style(typer.colors.BLUE, artist.disambiguation)}?")
            # Error Handling for non-int input
            try:
                artist_idx = int(typer.prompt("Which did you mean?"))
            except ValueError:
                typer.echo("Invalid Option Please enter a number")
                raise typer.Exit()
            return data.artists[artist_idx]
        else:
            return data.artists[0]
    else:
        typer.echo(data)


def find_song_list(found_artist):
    """ get list of unique song titles related to artist """
    total = 1000
    with typer.progressbar(length=total, label=style(typer.colors.GREEN, "Getting Songs")) as progress:
        success, data = musicbrainz.get_release_list(found_artist)
        song_list = []
        for idx, release in enumerate(data.releases):
            success, songs = musicbrainz.get_song_list(release)
            progress.update(total/len(data.releases))
            try:
                for tracks in songs.media:
                    for track in tracks.tracks:
                        song_list.append(track.title)
            except:
                typer.echo(songs)
        # remove duplicate songs
        # I realise this a bit of a 'hacky' way of doing as it doesn't
        # remove parital duplicates but there could be extra words in there
        song_list = sorted(list(dict.fromkeys(song_list)))

    return song_list
