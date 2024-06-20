"""
Mappers transform plain dict to another dict
converting key and values.

Classes definition are inspired on pydantic
"""

import sys
import traceback

from dateutil.parser import parse
from dateutil.tz import gettz

from syncmodels.mapper import *
from ..models import beacons

# ---------------------------------------------------------
# Loggers
# ---------------------------------------------------------

from agptools.logs import logger

log = logger(__name__)


# =========================================================
# BeaconsTrace Mappers
# =========================================================


# ---------------------------------------------------------
# Base Mappers Classes
# ---------------------------------------------------------
def FOO_GUESS_IBSK_TYPE(x):
    m = re.match(r"(iBKSPlus|IBKS105)", x)
    if m:
        return m.group(0)


class BeaconDataTrace(Mapper):
    PYDANTIC = beacons.BeaconDataSet

    mac = r"mac|id", I
    date = I, DATE, ""

