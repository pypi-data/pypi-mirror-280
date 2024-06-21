#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2023-10-25
# @Filename: dataclasses.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

from __future__ import annotations

from dataclasses import dataclass


__all__ = ["APOData"]


@dataclass
class APOData:
    pressure: float = -999.0
    windd: float = -999.0
    winds: float = -999.0
    gustd: float = -999.0
    gusts: float = -999.0
    airtemp: float = -999.0
    dewpoint: float = -999.0
    dpErr: float = -999.0
    humidity: float = -999.0
    dusta: float = -999.0
    dustb: float = -999.0
    dustc: float = -999.0
    dustd: float = -999.0
    windd25m: float = -999.0
    winds25m: float = -999.0
    encl25m: int = 0
    truss25m: float = -999.0
    airTempPT: float = -999.0
    dpTempPT: float = -999.0
    humidPT: float = -999.0
    dimmflux1: float = -999.0
    dimmflux2: float = -999.0
    irscmean: float = -999.0
    irscsd: float = -999.0


@dataclass
class TPMData:
    airTempPT: float = -999.0
    dpTempPT: float = -999.0
    humidPT: float = -999.0
    truss25m: float = -999.0
    winds25m: float = -999.0
    windd25m: float = -999.0
    encl25m: int = 0
