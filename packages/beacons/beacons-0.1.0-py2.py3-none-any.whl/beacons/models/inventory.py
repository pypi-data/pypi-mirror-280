"""
This file supports Inventory Pattern for beacons

From Inserious Team, the specification of a beacon is as follows:

(mail from 2024-03-27)

|                    |     |                      |                                                                                          |
| ------------------ | --- | -------------------- | ---------------------------------------------------------------------------------------- |
| **EP Beacon/QR**   |     |                      |                                                                                          |
| _Group_            |     | _Data_               | _Observaciones_                                                                          |
| ------------------ | --- | -------------------- | ---------------------------------------------------------------------------------------- |
| Beacon             | *   | device_name          | Debe obviamente ser único                                                                |
|                    | *   | device_type          | Actualmente IKBS 105 ó IKBS PLUS                                                         |
|                    | *   | uuid                 | 32 bytes conforme al slot de transmisión                                                 |
|                    | *   | advertising_interval | Milliseconds conforme al slot de transmisión                                             |
|                    | *   | TX_power             | Conforme al slot de transmisión                                                          |
|                    |     | url                  | Opcional. No para uso inicial                                                            |
| QR                 | *   | key_content          | Texto-ID para su lectura                                                                 |
| Geolocation        | *   | lan                  |                                                                                          |
|                    | *   | lng                  |                                                                                          |
| Ubication          | *   | ubication            | MUSEO ó GR330 inicialmente (conforme al Anexo II del PPT y uso por las Apps)             |
| Associated_content | *   | id                   |                                                                                          |
|                    | *   | entity               | Puede ser un RD cuando proceda                                                           |
|                    | *   | category             | Puede ser "" cuando proceda                                                              |
| Description        |     | description          | Opcional. Detalle sobre la ubicación o los contenidos, solo para uso informativo interno |

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

from .base import *

# from ..ports import *

from .beacons import *

# TODO: extend model corpus classes, a.k.a: the pydantic based thesaurus foundations classes
# TODO: this classes may be included in the main thesaurus when project is stable
# TODO: and others projects can benefit from them, making the thesaurus bigger and more powerful


# ---------------------------------------------------------
# InventoryItem
# ---------------------------------------------------------
# TODO: Inherit from smartmodels.model.inventory (or similar)
class BeaconInventoryItem(Item):
    """A Beacons Inventory Item model"""

    # beacon specific fields
    mac: str = Field(
        "",
        description="MAC address",
        examples=["CB8556F8CEC7", "E797F9BA67B7"],
    )
    type: str = Field(
        "IKBS 105",
        description="Beacon device type name",
        examples=["IKBS 105", "IKBS PLUS"],
    )
    advertising_interval: int = Field(
        10000,
        description="Milliseconds beam pulse",
        examples=[10000, 20000],
    )
    tx_power: int = Field(
        1,
        description="Transmission power",
        examples=[0, 1],  # TODO: check valid values
    )
    # QR specific fields
    key_content: str = Field(
        "",
        description="Text-ID for human reading",
        examples=["foo bar beacon", "buzz beacon"],
    )

    # Geolocation specific fields
    # Ubication
    # >> location: Location
    # location: Optional[Location] | None

    url: str = Field(
        "",
        description="content url",
        examples=[],
    )

    lat: float | None = Field(
        -0.4927112533945035,
        description="Latitude",
        examples=[-0.4927112533945035],
    )

    lng: float | None = Field(
        38.42381440278734,
        description="Longitude",
        examples=[38.42381440278734],
    )
    ubication: str = Field(
        "",
        description="beacon's ubication",
        examples=["LUCENTUM", "CAMPELLO"],
    )
    zone: str = Field(
        "",
        description="beacon's zone",
        examples=[
            "Sala Edad Media",
            "Sala Edad Moderna y Contemporanea",
            "Sala de Prehistoria",
            "Sala de Iberos",
        ],
    )

    # Content specific fields
    content_id: str = Field(
        "",
        description="????",
        examples=["??", "???"],
    )
    content_entity: str = Field(
        "",
        description="????",
        examples=["??", "???"],
    )
    content_category: str = Field(
        "",
        description="????",
        examples=["??", "???"],
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


class BeaconsInventory(Item):
    """A Beacons InventoryItem model"""

    item: Dict[UID_TYPE, BeaconInventoryItem] = {}


# ---------------------------------------------------------
# InventoryRequest
# ---------------------------------------------------------
class BeaconsInventoryRequest(Request):
    """A Beacons request to inventory manager.
    Contains all query data and search parameters
    (None for the current version).
    """

    filter: Dict[str, str] = Field(
        {},
        description="{key: value} inventory filter (both can be regular expressions). Multiples values are allowed using AND operator",
        examples=[
            {"name": r"MARQ-\d+", "zone": r".*prehistoria$"},
            {"name": r"MARQ"},
            {"name|zone": r".*MARQ.*"},
        ],
    )


# ---------------------------------------------------------
# InventoryResponse
# ---------------------------------------------------------
class BeaconsInventoryResponse(Response):
    """A Beacons response to inventory manager.
    Contains the search results given by a request.
    """

    num_items: int = Field(
        0,
        description="Number of items found",
    )
    # use list due INS claims
    # result: Dict[UID_TYPE, BeaconInventoryItem] = {}
    result: List[BeaconInventoryItem] = []


class BeaconsUpdateInventoryResponse(Response):
    """TBD"""

    result: Dict[str, int] = {}
