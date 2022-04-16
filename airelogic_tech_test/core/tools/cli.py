""" cli functions to improve typer output """

from typer import Typer

from core.tools.musicbrainz import find_artist, find_song_list
import typer


def lister(_list):
    typer.echo("-" * 50)
    typer.echo("|  {}  |  {}")


if __name__ == '__main__':
    app = typer.Typer()
