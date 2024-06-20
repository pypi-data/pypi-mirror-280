"""
Implement beacon logic

"""

# ---------------------------------------------------------
# Import models
# ---------------------------------------------------------
import asyncio
import re

# from typing import List

# from ..models.beacons import Person, MessageBox
from datetime import datetime

import sys
import traceback
import json


# from syncmodels.syncmodels import SyncModel
# from syncmodels.syncmodels import Transformer

# from swarmtube.definitions import MONOTONIC_KEY
# from swarmtube.logic.swarmtube import (
# SkipWave,
# RetryWave,
# )
from swarmtube.particles.fiware import OrionParticleSync


# from syncmodels.storage import SurrealistStorage

from agptools.logs import logger

from ..mappers.fiware import FiwareBeaconTrace

log = logger(__file__)


class BeaconsTracesOrionSync(OrionParticleSync):
    """A Particle that sync traces with Platform.

    {
      'beacons_models_beacons_BeaconTraceItem':
        {
          'date': '2024-05-06T08:33:09.603933',
          'device_id': '1xmNvtXCwvH5iluyIx3jB2eu2KpotK932gikml4SCcMq9wAb6YT3PV9p7KoYsZWYmtty7TrxE',
          'id': 'beacons_models_beacons_BeaconTraceItem:1714979406785624085',
          'id__': '',
          'lat': 38.42381440278734,
          'lng': -0.4927112533945035,
          'mac': '00:00:08:f3:1c:d0',
          'publish_date': '2024-05-06T08:35:09.603891',
          'wave__': 1714979406785624085,
        },
      'wave__': 1714979406785624085,
    }
    """

    MAPPER = FiwareBeaconTrace
