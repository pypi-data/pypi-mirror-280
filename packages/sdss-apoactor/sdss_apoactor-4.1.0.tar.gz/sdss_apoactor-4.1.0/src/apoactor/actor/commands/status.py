#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2023-10-25
# @Filename: status.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

from __future__ import annotations

from typing import TYPE_CHECKING

from clu.parsers.click import command_parser


if TYPE_CHECKING:
    from .. import APOCommandType


@command_parser.command()
async def status(command: APOCommandType):
    """Outputs the status values."""

    await command.actor.output_status(command)
    return command.finish()


@command_parser.command()
async def update(command: APOCommandType):
    """Alias for status. Kept for historical reasons.."""

    await command.actor.output_status(command)
    return command.finish()
