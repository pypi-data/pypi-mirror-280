import click
from .create import create
from .get_paginated import get_paginated
from .get_single import get_single
from .update import update
from .delete import delete

@click.group(name='projects')
def projects():
    """Commands to manage projects."""
    pass

projects.add_command(create)
projects.add_command(get_paginated)
projects.add_command(get_single)
projects.add_command(update)
projects.add_command(delete)

__all__ = ['projects']
