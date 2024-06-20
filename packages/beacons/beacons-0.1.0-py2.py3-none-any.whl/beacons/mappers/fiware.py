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
from ..models import fiware

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


class FiwareBeaconTrace(Mapper):
    PYDANTIC = fiware.FiwareBeaconTrace

    id = I, I
    type = I, I  # , "beacons.traces"
    ts = I, I

    mac = I, I
    date = I, DATE, ""
    publish_date = I, DATE
    device_id = I, I
    location = I, I

    battery_level = I, INT, 100
    installation_date = I, DATE, None
    last_reset_date = I, DATE, None
    last_update_date = I, DATE, None
