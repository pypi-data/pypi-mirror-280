"""
This module contains all Models used to interact with the outside world
no matter is it comes from an API REST interface or CLI interface.

In CLI case, a pretty print method will enrich the console output.

The code placed here should be an abstraction / base / common code
for any specific port implementation to connect to external systems
such FastAPI, CLI (Click), MQTT protocols, etc.

Some rules are:

- This code must support the way to communicate with external world related to `beacons` example
- This code may not implement any business logic or uses cases, just being an abstraction of
how we need to communicate the outside world, no mather the mechanism / protocols used.
- Specific subclasses / submodules will implement this template classes.

"""

from datetime import datetime, timedelta
from dateutil.parser import parse

from typing import Union, List, Tuple
from typing_extensions import Annotated


from syncmodels.model import BaseModel, field_validator, Field
from syncmodels.mapper import *

# from models.generic.price import PriceSpecification
# from models.generic.schedules import OpeningHoursSpecificationSpec

# from ..enums import *


# ---------------------------------------------------------
# Request and Response Ports
# ---------------------------------------------------------

# TODO: define any port/adaptor classes needed to communicate
# TODO: with external interface / adapters: FastAPI, CLI, etc


# ---------------------------------------------------------
# A typical request specification Ports model
# ---------------------------------------------------------
class BeaconsRequest(BaseModel):
    # geojson: GeoJSON
    # interests: Annotated[List[WeightedInterest], "user specific interests"] = []
    include: Annotated[
        List[str], "acts as include filter, based on flexible `dti` search on values"
    ] = []
    exclude: Annotated[
        List[str], "acts as exclude filter, based on flexible `dti` search on values"
    ] = []
    max_distance: Annotated[
        int, "the max distance in metres from the location *center*"
    ] = 1000
    limit: Annotated[int, "max returned items"] = 10
    sort: Annotated[
        bool, "whenever items must be ordered by distance from the *center"
    ] = True


class BeaconsResponse(BaseModel):
    elapsed: float = -1
    # candidates: Dict[str, Candidate] = {}
