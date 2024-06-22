import click
from .create import create
from .get_paginated import get_paginated
from .get_single import get_single
from .update import update
from .delete import delete

@click.group(name='tags')
def tags():
    """Commands to manage tags."""
    pass

tags.add_command(create)
tags.add_command(get_paginated)
tags.add_command(get_single)
tags.add_command(update)
tags.add_command(delete)

__all__ = ['tags']
