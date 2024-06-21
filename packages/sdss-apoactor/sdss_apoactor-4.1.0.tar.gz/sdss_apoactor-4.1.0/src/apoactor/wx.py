#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2023-10-25
# @Filename: wx.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

from __future__ import annotations

import asyncio
import binascii
import ctypes
import re

from asyncudp import create_socket

from apoactor import config


__all__ = ["WX"]


def uint(x: int):
    """Converts a signed integer to an unsigned integer."""

    return ctypes.c_uint(x).value


class WXError(Exception):
    """WX error."""

    pass


class WX:
    """Retrieves data from the WX server."""

    def __init__(self):
        wx_server_config = config["wx_server"].copy()

        self.host: str = wx_server_config["host"]
        self.port: int = wx_server_config["port"]
        self.timeout: float = wx_server_config["timeout"]
        self.keys: list[str] = wx_server_config["keys"]

    async def get_raw_data(self):
        """Retrieves the tuples string from the WX server."""

        socket = await asyncio.wait_for(
            create_socket(remote_addr=(self.host, self.port)),
            timeout=self.timeout,
        )

        try:
            socket.sendto(b"tuples")

            reply = await asyncio.wait_for(socket.recvfrom(), timeout=self.timeout)
            assert isinstance(reply[0], bytes)

            self.validate(reply[0].decode())
        except Exception as ee:
            raise WXError(f"Error retrieving data: {ee}")
        finally:
            socket.close()

        return reply[0].decode()

    def validate(self, reply: str):
        """Validates the reply."""

        if "end" != reply[-3:]:
            raise WXError("Premature end of data")

        start = reply.find("timeStamp")
        stop = reply.find(" end")
        length, crc32, nvals = reply[:start].split()

        reply_bytes = reply[start:].encode()

        if start == -1:
            raise WXError("'timeStamp' key not found.")
        elif -1 == stop:
            raise WXError("'end' key not found.")
        elif int(length) != len(reply[start:]):
            raise WXError("Short packet.")
        elif int(crc32, 16) != uint(0xFFFFFFFF & binascii.crc32(reply_bytes)):
            raise WXError("Invalid CRC32.")
        elif int(nvals) != len(reply[start:stop].split()):
            raise WXError("Missing value(s).")

    async def get_dict(self, return_all_keys: bool = True):
        """Returns a dictionary of values."""

        reply = await self.get_raw_data()

        value_pattern = re.compile(r"([a-zA-Z0-9_]+)\=\([0-9]+,\'(.+?)\'\)")

        groups = re.findall(value_pattern, reply)
        groups_dict = {key: value for key, value in groups}

        if return_all_keys:
            keys = groups_dict.keys()
        else:
            keys = self.keys
            groups_dict = {key.lower(): value for key, value in groups_dict.items()}

        dd: dict[str, int | float | str] = {}
        for key in keys:
            if key.lower() in groups_dict:
                value = groups_dict[key.lower()]

                try:
                    value = int(value)
                except ValueError:
                    try:
                        value = float(value)
                    except ValueError:
                        pass

                if key.startswith("dust") and isinstance(value, str):
                    # Replace dpDep with -999.0
                    value = -999.0

                dd[key] = value

        return dd
