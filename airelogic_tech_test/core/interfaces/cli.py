""" cli interface functions """

import typer


def style(colour=typer.colors.RED, string=""):
    return typer.style(string, fg=colour, bold=True)
