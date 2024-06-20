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
from ..models import inventory

# ---------------------------------------------------------
# Loggers
# ---------------------------------------------------------

from agptools.logs import logger

log = logger(__name__)


# =========================================================
# BeaconsInventory Mappers
# =========================================================


# ---------------------------------------------------------
# Base Mappers Classes
# ---------------------------------------------------------
def GUESS_IBSK_TYPE(x):
    m = re.match(r"(iBKSPlus|IBKS105)", x)
    if m:
        return m.group(0)


class BeaconItem(Mapper):
    PYDANTIC = inventory.BeaconInventoryItem
    id = r"uid|Data\s+S0", I
    name = r"Device\s*Name", I, ""
    description = r"Zona", I, ""

    mac = r"MAC\s+Address", I
    type = r"iBKS\s+Serial", GUESS_IBSK_TYPE
    advertising_interval = r"Advertising.*S0$", I
    tx_power = r"Tx.*Power.*IB.*S0$", I, 1

    url = r"url", I, ""
    lat = r"Latitud", FLOAT, ""
    lng = r"Longitud", FLOAT, ""
    ubication = r"Lugar", I, ""
    zone = r"Zona", I, ""

    key_content = I, I, ""
    content_id = I, I, ""
    content_entity = I, I, ""
    content_category = I, I, ""


class BeaconsInventory(Mapper):
    PYDANTIC = inventory.BeaconsInventory
