#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2023-10-22
# @Filename: __main__.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

from __future__ import annotations

import os
import sys

import click
from click_default_group import DefaultGroup

from clu.tools import cli_coro
from sdsstools.daemonizer import DaemonGroup

from apoactor import __version__
from apoactor.actor import APOActor


@click.group(
    cls=DefaultGroup,
    default="actor",
    default_if_no_args=True,
    invoke_without_command=True,
)
@click.option(
    "--version",
    is_flag=True,
    help="Print version and exit.",
)
def apoactor(version: bool = False):
    """APO actor."""

    if version is True:
        click.echo(__version__)
        sys.exit(0)


@apoactor.group(cls=DaemonGroup, prog="apo-actor", workdir=os.getcwd())
@click.pass_context
@cli_coro
async def actor(ctx: click.Context):
    """Runs the actor."""

    default_config_file = os.path.join(os.path.dirname(__file__), "etc/apoactor.yml")
    apo_obj = APOActor.from_config(default_config_file)

    await apo_obj.start()
    await apo_obj.run_forever()


if __name__ == "__main__":
    apoactor()
