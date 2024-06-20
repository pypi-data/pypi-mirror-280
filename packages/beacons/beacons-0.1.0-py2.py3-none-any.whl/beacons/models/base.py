"""
This file supports Base Items Pattern for beacons
"""

from datetime import datetime, timedelta
import random
import uuid
from dateutil.parser import parse

from typing import Union, List, Tuple, Dict
from typing_extensions import Annotated


from syncmodels.model import BaseModel, field_validator, Field
from syncmodels.mapper import *

# from models.generic.price import PriceSpecification
# from models.generic.schedules import OpeningHoursSpecificationSpec

from beacons.definitions import UID_TYPE

# =========================================================
# A base Beacons classes
# =========================================================
# TODO: extend model corpus classes, a.k.a: the pydantic based thesaurus foundations classes
# TODO: this classes may be included in the main thesaurus when project is stable
# TODO: and others projects can benefit from them, making the thesaurus bigger and more powerful


# ---------------------------------------------------------
# A base Item
# ---------------------------------------------------------
# TODO: Inherit from smartmodels.model.base (or similar)
class Item(BaseModel):
    """A Beacons InventoryItem model"""

    id: UID_TYPE = Field(
        description="beacons unique identifier",
        examples=[
            "4262BBEDFFB60AF9EE0D0A5E00000088",
            "4262BBEDFFB60AF9EE0D0A5E0000008B",
            "4262BBEDFFB60AF9EE0D0A5E00000084",
        ],
    )
    name: Optional[str] | None = Field(
        "",
        description="beacons name",
        examples=[
            "nice-item",
        ],
    )
    description: Optional[str] | None = Field(
        "",
        description="beacons human more descriptive name",
        examples=[
            "A Nice Item",
        ],
    )

    @field_validator("id")
    def convert_id(cls, value):
        if not isinstance(value, UID_TYPE):
            value = UID_TYPE(value)
        # TODO: make some validations here
        return value


# ---------------------------------------------------------
# A base Request
# ---------------------------------------------------------
class Request(BaseModel):
    """A Beacons request to task manager.
    Contains all query data and search parameters.
    """


# ---------------------------------------------------------
# A base Response
# ---------------------------------------------------------
class Response(BaseModel):
    """A Beacons response to task manager.
    Contains the search results given by a request.
    """

    elapsed: float = Field(
        0,
        description="computation elapsed time",
        examples=[
            0,
        ],
    )
    result: Dict[UID_TYPE, Item] = {}


# =========================================================
# A base BeaconsInventory
# =========================================================


# ---------------------------------------------------------
# A base BeaconsTask
# ---------------------------------------------------------
class Inventory(Item):
    pass


# =========================================================
# A base BeaconsTask
# =========================================================


# ---------------------------------------------------------
# A base BeaconsTask
# ---------------------------------------------------------
class Task(Inventory):
    pass


# =========================================================
# A base BeaconsScript
# =========================================================


# ---------------------------------------------------------
# A base BeaconsScript
# ---------------------------------------------------------
class Script(Inventory):
    pass
