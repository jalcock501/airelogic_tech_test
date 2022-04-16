""" Tests for CLI """

import typer
from typer.testing import CliRunner

from airelogic_tech_test.core.tools.musicbrainz import find_artist

app = typer.Typer()
app.command()(find_artist)
runner = CliRunner()


def test_cli():
    """ Test that runner returns correct artist and cli functionality """
    result = runner.invoke(app, ["Nirvana"], input="0")
    assert result.exit_code == 0
    assert "0: Nirvana the 90s US grunge band?" in result.stdout
