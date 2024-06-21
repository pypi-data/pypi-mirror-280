#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2023-10-25
# @Filename: tpm.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

from __future__ import annotations

import asyncio

from typing import Any

import numpy
from tpm_multicast_client import listen_to_multicast

from apoactor.dataclasses import TPMData


class TPM:
    """Monitors the TPM broadcast."""

    def __init__(self):
        self.queue = asyncio.Queue[TPMData](maxsize=5)

        self.protocol: asyncio.DatagramProtocol | None = None
        self.transport: asyncio.DatagramTransport | None = None

    async def start(self):
        """Starts listening to the multicast."""

        self.transport, self.protocol = await listen_to_multicast(self.process)

    async def stop(self):
        """Closes the transport."""

        if self.transport is None:
            raise RuntimeError("The transport is not defined.")

        self.transport.close()

    async def process(self, data: dict[str, Any]):
        """Processes the datagram."""

        try:
            tpm_data = TPMData(
                airTempPT=data["DpTempA"],
                dpTempPT=data["DpTempB"],
                humidPT=self.get_humidity(data),
                truss25m=self.get_truss(data),
                encl25m=self.get_enclosure(data),
            )

            self.queue.put_nowait(tpm_data)

        except Exception:
            pass

    def get_humidity(self, data: dict[str, Any]):
        """Calculates the humidity."""

        dpA = data["DpTempA"]
        dpB = data["DpTempB"]

        humid = 100.0 * (
            numpy.exp((17.625 * dpB) / (243.04 + dpB))
            / numpy.exp((17.625 * dpA) / (243.04 + dpA))
        )

        if humid > 100:
            humid = 100.0
        if humid < 0:
            humid = 0.0

        return humid

    def get_truss(self, data: dict[str, Any]):
        """Calculates the truss temperature."""

        temp: float = 0.0

        for ii in range(0, 8):
            temp += data[f"therm1_{24+ii}"]

        return numpy.round(temp / 8, 2)

    def get_enclosure(self, data: dict[str, Any]):
        """Returns whether the enclosure is open."""

        bldg_clear_az = (data["plc_words_158"] & 0x10) != 0
        bldg_clear_alt = (data["plc_words_157"] & 0x02) != 0

        if bldg_clear_az & bldg_clear_alt:
            return 1  # 1 means open

        return 0  # 0 means closed
