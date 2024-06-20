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
from syncmodels.mapper import *

from syncmodels.helpers.faker import fake

# from models.generic.price import PriceSpecification
# from models.generic.schedules import OpeningHoursSpecificationSpec

from .base import *

# TODO: extend model corpus classes, a.k.a: the pydantic based thesaurus foundations classes
# TODO: this classes may be included in the main thesaurus when project is stable
# TODO: and others projects can benefit from them, making the thesaurus bigger and more powerful


# ---------------------------------------------------------
# BeaconItem
# ---------------------------------------------------------
# TODO: Inherit from smartmodels.model.app (or similar)
class BeaconItem(Item):
    """A Beacons Item model"""


# ---------------------------------------------------------
# A base BeaconsRequest
# ---------------------------------------------------------
class BeaconsRequest(Request):
    """A Beacons request to task manager.
    Contains all query data and search parameters.
    """


# ---------------------------------------------------------
# A base BeaconsResponse
# ---------------------------------------------------------
class BeaconsResponse(Response):
    """A Beacons response to task manager.
    Contains the search results given by a request.
    """

    data: Dict[UID_TYPE, BeaconItem] = {}


# ---------------------------------------------------------
# BeaconsApp
# ---------------------------------------------------------
# TODO: Inherit from smartmodels.model.app (or similar)
class BeaconsApp(Item):
    """A Beacons App model"""

    pass


# ---------------------------------------------------------
# Foundations Model classes
# (maybe from global model repository)
# ---------------------------------------------------------
class GeoJSON(BaseModel):
    """GeoJSON Specification.
    By default, GeoJSON type is a Point with a single coordinates pair
    of (longitude, latitude) values.
    """

    type: str = "Point"
    coordinates: List[List[float]] | List[float] = [
        -0.4927112533945035,
        38.42381440278734,
    ]


# ---------------------------------------------------------
# Another group of Model classes with default values
# to be easily represented in FastAPI for instance
# ---------------------------------------------------------


class Location(BaseModel):
    """A GeoJSON Location with additional information"""

    address: str | None = None
    # geojson: GeoJSON | None = None
    lng: float = -0.4927112533945035
    lat: float = 38.42381440278734


DEFAULT_LOCATION = Location(
    address="Plaça de Baix, 1, 03202 Elx, Alicante",
    lng=-0.6989062426179778,
    lat=38.26566276366765,
)


# ---------------------------------------------------------
# Beacon relate Model classes
# ---------------------------------------------------------
class BeaconTrace(BaseModel):
    """A Beacon Trace"""

    id: Optional[str] | None = Field(
        "",
        description="`mac` address of beacon by default",
        examples=["CB:85:56:F8:CE:C7", "E7:97:F9:BA:67:B7"],
    )
    mac: str = Field(
        description="`mac` address of beacon",
        examples=["CB:85:56:F8:CE:C7", "E7:97:F9:BA:67:B7"],
    )
    date: datetime = Field(
        description="Datetime when mobile app detect the beacon",
        examples=["2024-03-24T20:00:00Z"],
    )
    # location: Location | None = None
    lng: float = Field(
        -0.4927112533945035,
        description="latitude coordinate of mobile app when detect the beacon",
        examples=[-0.4927112533945035],
    )
    lat: float = Field(
        38.42381440278734,
        description="longitude coordinate of mobile app when detect the beacon",
        examples=[38.42381440278734],
    )

    # Battery specific fields
    battery_level: Optional[int] | None = Field(
        100,
        description="Beacon's battery level (from 0-100)",
        examples=[100],
    )

    # Extra fields
    installation_date: Optional[Datetime] | None = Field(
        None,
        description="Beacon's installation date",
        examples=["2024-03-24T20:00:00Z"],
    )
    last_reset_date: Optional[Datetime] | None = Field(
        None,
        description="Beacon's last reset date",
        examples=["2024-03-24T20:00:00Z"],
    )
    last_update_date: Optional[Datetime] | None = Field(
        None,
        description="Beacon's last update date",
        examples=["2024-03-24T20:00:00Z"],
    )


def random_trace(n=10):
    result = []
    n = random.randint(1, n + 1)
    start = datetime.now() - timedelta(seconds=120)
    for _ in range(n):
        mac = fake.hexify(text="00:00:^^:^^:^^:^^")
        item = BeaconTrace(
            mac=mac,
            date=start,
        )
        start = start + timedelta(seconds=2)
        result.append(item)
    return result


class BeaconDataSet(BaseModel):
    """A Beacon data set model.
    This data set contains Beacons trace information
    and the datetime associated with the publishing attempt.
    """

    device_id: str = Field(
        description="unique device identifier (not needed to be related to any personal data)",
        examples=[],
        pattern=r"^\w+$",
    )
    publish_date: datetime | None = Field(
        description="date of publishing attempt",
        examples=[datetime.now()],
    )
    traces: List[BeaconTrace] = Field(
        description="List of traces",
        examples=[random_trace()],
    )


class BeaconTraceSet(BeaconTrace):
    """Expand BeaconTrace with data from mobile-id and publish_date"""

    device_id: str = Field(
        description="unique device identifier (not needed to be related to any personal data)",
        examples=[],
        pattern=r"^\w+$",
    )
    publish_date: datetime | None = Field(
        description="date of publishing attempt",
        examples=[datetime.now()],
    )


class BeaconTraceItem(BeaconTraceSet):
    """A Beacon Trace Item (has id)"""

    # TODO: move to syncmodels to derive from
    # from symcmodels.definitions.MONOTONIC_KEY
    # wave__: Optional[int] | None = Field(
    # 0,
    # description="Internal monotonic insertion key",
    # examples=[],
    # )

    # id: Optional[str] | None = Field(
    # "",
    # description="Internal Trace id",
    # examples=[],
    # )


# ---------------------------------------------------------
# InventoryRequest
# ---------------------------------------------------------
class BeaconsDataSetRequest(Request):
    """A Beacons request to inventory manager.
    Contains all query data and search parameters
    (None for the current version).
    """

    filter: Dict[str, str] = Field(
        {},
        description="{key: value} inventory filter (both can be regular expressions). Multiples values are allowed using AND operator",
        examples=[],
    )


# ---------------------------------------------------------
# InventoryResponse
# ---------------------------------------------------------
class BeaconsDataSetResponse(Response):
    """A Beacons response to inventory manager.
    Contains the search results given by a request.
    """

    num_items: int = Field(
        0,
        description="Number of items found",
    )
    # result: Dict[UID_TYPE, BeaconDataSet] = {}
    result: List[BeaconTraceSet] = []


# ---------------------------------------------------------
# Some examples of other demo Model classes
# TODO: delete / replace (just for educational purposes)
# ---------------------------------------------------------
class BeaconsPreferences(BaseModel):
    """Beacon Backend Preferences"""

    publish_rate: int = Field(
        description="Number of seconds between publishing stored data",
        examples=[240, 300],
    )
    publish_on_start: bool = Field(
        description="If app will publish non-flushed data when application starts",
        examples=[True, False],
    )
    publish_on_stop: bool = Field(
        description="If app may try to publish non-flushed data before application closes",
        examples=[True, False],
    )
    publish_timeout: int = Field(
        description="Number of seconds to consider the server is not responding",
        examples=[5, 8],
    )
    publish_max_traces: int = Field(
        description="Maximum number of beacon traces sent in single message",
        examples=[50, 100],
    )
    # @field_validator("start", "end")
    # def convert_datetime(cls, value):
    #     if isinstance(value, str):
    #         value = parse(value)
    #     return value


# ---------------------------------------------------------
# Main Model Class
# This represents the state of the whole application
# ---------------------------------------------------------
class BeaconAppRepresentation(BaseModel):
    """Example of an possible Beacon App Internal representation."""

    id: str
    name: str
    # summary: Optional[str] = ""
    # image_url: Optional[str] = ""
    # location: Location | dict | None = None
    # tags: Optional[List[str]] = []
    # time_table: Optional[OpeningHoursSpecification] | None = None
