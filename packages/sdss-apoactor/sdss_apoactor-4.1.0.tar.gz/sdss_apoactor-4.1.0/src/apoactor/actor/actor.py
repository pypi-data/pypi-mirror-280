#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2023-10-22
# @Filename: actor.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

from __future__ import annotations

import asyncio
import pathlib

from typing import TYPE_CHECKING, Self

import numpy

from clu.legacy import LegacyActor

from apoactor import __version__, log
from apoactor.dataclasses import APOData
from apoactor.tool import get_volume_info
from apoactor.tpm import TPM
from apoactor.wx import WX


if TYPE_CHECKING:
    from clu.command import Command


__all__ = ["APOActor"]


class APOActor(LegacyActor):
    """APO actor."""

    def __init__(self, *args, **kwargs):
        self.observatory = "APO"

        schema = pathlib.Path(__file__).parents[1] / "etc/schema.json"

        super().__init__(*args, schema=schema, log=log, **kwargs)

        self.version = __version__

        self.output_periodic_task: asyncio.Task | None = None

        self.monitor_tpm_task: asyncio.Task | None = None
        self.tpm = TPM()

        self.wx = WX()

        self.data = APOData()

    async def start(self, get_keys: bool = True, start_nubs: bool = True) -> Self:
        """Starts the actor."""

        await self.reconnect_tpm()
        self.output_periodic_task = asyncio.create_task(self.output_periodic())

        return await super().start(get_keys, start_nubs)

    async def reconnect_tpm(self):
        """Recreates the connection to the TPM broadcast."""

        if self.monitor_tpm_task is not None and not self.monitor_tpm_task.done():
            self.monitor_tpm_task.cancel()

        if self.tpm.transport:
            await self.tpm.stop()

        self.monitor_tpm_task = asyncio.create_task(self.monitor_tpm())

    async def monitor_tpm(self):
        """Monitors the TPM broadcast and updates the data class."""

        await self.tpm.start()

        while True:
            tpm_data = await self.tpm.queue.get()

            self.data.__dict__.update(tpm_data.__dict__)

    async def update_wx_data(self):
        """Updates the data class."""

        wx_data = await self.wx.get_dict(return_all_keys=False)
        self.data.__dict__.update(wx_data)

    async def output_periodic(self):
        """Outputs the status on a timer."""

        delay: float = self.config["status_delay"]

        # Wait a few seconds before the first output. This gives time to the
        # TPM to output at least one message.
        await asyncio.sleep(5)

        while True:
            try:
                await self.output_status()
            except Exception as err:
                self.write("w", error=f"Failed outputting periodic status: {err}")

            await asyncio.sleep(delay)

    async def output_status(self, command: Command | None = None):
        """Outputs the status of the enclosure."""

        # Output weather and enclosure data.
        await self.update_wx_data()
        self.write(message_code="i", message=self.data.__dict__, command=command)

        # Output volume data.
        for volume in self.config["volumes"]:
            size, free = get_volume_info(volume)

            ratio = free / size
            message_code = "w" if ratio < 0.1 else "i"

            self.write(
                message_code=message_code,
                message={"diskspace": ["sdss5-hub", volume, int(size), int(free)]},
                command=command,
            )

        await self.update_tcc(command)

    async def update_tcc(self, command: Command | None = None):
        """Updates the TCC with weather information."""

        tcc_config = self.config["tcc"].copy()

        if tcc_config["send_to_tcc"] is False:
            return

        tcc_strings = []
        for wx_name, tcc_name in tcc_config["wx_to_tcc_names"].items():
            value = self.data.__dict__[wx_name]

            # The TCC uses pressure in Pascals and humidity as a fraction of one
            # so we convert from inHg -> Pascals and % -> fraction respectively.
            if wx_name == "pressure":
                value = numpy.round(3386.3788 * value, 3)
            if wx_name == "humidPT":
                value = numpy.round(0.01 * value, 3)

            tcc_strings.append(f"{tcc_name}={value}")

        command_string = "set weather " + (", ".join(tcc_strings))

        if command:
            await command.send_command("tcc", command_string)
        else:
            cmd = await self.send_command("tcc", command_string)
            await cmd
