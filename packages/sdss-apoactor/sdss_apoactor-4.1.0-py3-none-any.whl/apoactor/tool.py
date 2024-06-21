#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2023-10-25
# @Filename: tool.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

from __future__ import annotations

import os


__all__ = ["get_volume_info"]


def get_volume_info(volume: str):
    """Returns volume size and free size, in GB."""

    one_gig = 1024 * 1024 * 1024.0

    fsinfo = os.statvfs(volume)
    fssize = fsinfo.f_frsize * fsinfo.f_blocks / one_gig
    fsfree = fsinfo.f_frsize * fsinfo.f_bavail / one_gig

    return fssize, fsfree
