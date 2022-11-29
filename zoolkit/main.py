import click
import questionary
from .generators import create_dpy_bot, create_dpy_cog

@click.group()
def cli():
    return


@cli.command()
def dpy():
    refiend_ans = []
    category = questionary.select("What you want to create?", ['Bot', 'Cog']).ask()
    if category == 'Bot':
        bot_name = questionary.text("What is your project name?").ask()
        create_dpy_bot(name=bot_name)
    elif category == 'Cog':
        cog_name = questionary.text("What is your cog name?").ask()
        create_dpy_cog(name=cog_name)
