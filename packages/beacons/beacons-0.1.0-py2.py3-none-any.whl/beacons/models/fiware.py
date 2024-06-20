"""
This file supports Inventory Pattern for beacons
"""

from datetime import datetime, timedelta
import random
import uuid
from dateutil.parser import parse

from typing import Union, List, Tuple, Dict
from typing_extensions import Annotated


from syncmodels.model import BaseModel, field_validator, Field, Optional
from .beacons import BeaconTraceSet
from syncmodels.mapper import *

from syncmodels.helpers.faker import fake

# from models.generic.price import PriceSpecification
# from models.generic.schedules import OpeningHoursSpecificationSpec

from .base import *

# TODO: extend model corpus classes, a.k.a: the pydantic based thesaurus foundations classes
# TODO: this classes may be included in the main thesaurus when project is stable
# TODO: and others projects can benefit from them, making the thesaurus bigger and more powerful


# ---------------------------------------------------------
# Beacon relate Model classes
# ---------------------------------------------------------
class OrionItem(BaseModel):
    id: str = Field(
        description="`mac` address of beacon",
        examples=["CB:85:56:F8:CE:C7", "E7:97:F9:BA:67:B7"],
    )
    type: str = Field(
        "",
        description="`Fiware-Type`",
        # examples=[
        # "",
        # ],
    )
    ts: str = Field(
        description="timestamp in %Y-%m-%dT%H:%M:%S.%f with miliseconds",
    )


# TODO: take shared part from beacons.models
class FiwareBeaconTrace(OrionItem):
    """A Beacon Trace"""

    mac: str = Field(
        description="`mac` address of beacon",
        examples=["CB:85:56:F8:CE:C7", "E7:97:F9:BA:67:B7"],
    )
    date: datetime | None = Field(
        description="date when beacon was seen",
        examples=[datetime.now()],
    )
    publish_date: datetime | None = Field(
        description="date of publishing attempt",
        examples=[datetime.now()],
    )
    device_id: str = Field(
        description="unique device identifier (not needed to be related to any personal data)",
        examples=[],
        pattern=r"^\w+$",
    )
    location: str = Field(
        description="location in `geo:point` format",
    )

    battery_level: Optional[int] | None = Field(
        100,
        description="Beacon's battery level (from 0-100)",
        examples=[100],
    )

    # Extra fields
    installation_date: Optional[Datetime] | None = Field(
        None,
        description="Beacon's installation date",
        examples=["2024-03-24"],
    )
    last_reset_date: Optional[Datetime] | None = Field(
        None,
        description="Beacon's last reset date",
        examples=["2024-03-24"],
    )
    last_update_date: Optional[Datetime] | None = Field(
        None,
        description="Beacon's last update date",
        examples=["2024-03-24"],
    )
