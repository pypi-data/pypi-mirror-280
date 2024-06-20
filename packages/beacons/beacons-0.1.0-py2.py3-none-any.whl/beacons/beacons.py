"""Main beacons module.

Contains the FastAPI REST component

"""

# =========================================================
# beacons
# =========================================================

# ---------------------------------------------------------
# python library modules
# ---------------------------------------------------------

import asyncio

# import json
# import pickle
# import random
# import re
# import requests
import os
import random
import re
import sys
import traceback
import time
import yaml

# ---------------------------------------------------------
# partial imports
# ---------------------------------------------------------
from time import sleep

# from glom import glom  # , assign, T, merge


# ---------------------------------------------------------
# 3rd party libraries
# ---------------------------------------------------------

import uvicorn

# ---------------------------------------------------------
# 3rd party helpers
# ---------------------------------------------------------
from agptools.containers import walk, rebuild, overlap  # , diff, flatdict


# ---------------------------------------------------------
# local imports
# ---------------------------------------------------------

from .helpers import expandpath, parse_uri

# dynamic module loaders
from .helpers.loaders import ModuleLoader

# ---------------------------------------------------------
# Sync Models
# ---------------------------------------------------------
# from syncmodels.parallel import Parallel
# from syncmodels.syncmodels import SyncModel


# ---------------------------------------------------------
# enums
# ---------------------------------------------------------
# from .enums import POIEntitiesEnum


# ---------------------------------------------------------
# models / mappers
# ---------------------------------------------------------
# from .models import *
# from . import mappers


# local imports
# from .helpers import parse_uri

# ---------------------------------------------------------
# wing ide remote debug
# ---------------------------------------------------------
from .cli import main

# ---------------------------------------------------------
# Loggers
# ---------------------------------------------------------

from agptools.logs import logger

log = logger(__name__)

# subloger = logger(f'{__name__}.subloger')

# ---------------------------------------------------------
# fastAPI libraries
# ---------------------------------------------------------

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


# from starlette import status

# =========================================================
# beacons App
# =========================================================

# ---------------------------------------------------------
# routers
# ---------------------------------------------------------
# user specific EPs
# from .api.ports import publish

# common patterns EPs
# from .api.ports import config
# from .api.ports import inventory
# from .api.ports import search
# from .api.ports import stats
# from .api.ports import script
# from .api.ports import tasks

# AVAILABLE_PORTS = [
#     inventory,
#     tasks,
#     script,
#     publish,
#     search,
#     stats,
#     config,
# ]

# ---------------------------------------------------------
# Load active port (FastAPI routers) modules
# from `config.yaml` config file
# ---------------------------------------------------------

# from .cli import main
from .api import ports

loader = ModuleLoader(ports)
names = loader.available_modules()
ACTIVE_PORTS = loader.load_modules(names)

openapi_tags = []
for port in ACTIVE_PORTS:
    if hasattr(port, "TAG"):
        openapi_tags.append(
            {
                "name": port.TAG,
                "description": port.DESCRIPTION,
                "order": port.API_ORDER,
            }
        )

ACTIVE_PORTS.sort(key=lambda x: getattr(x, "API_ORDER", 1000), reverse=True)

# ---------------------------------------------------------
# Create FastAPI application
# ---------------------------------------------------------

app = FastAPI(
    title="beacons",
    description="""
    Smart beacons API

    FIWARE [Smart Data Models](https://www.fiware.org/smart-data-models/)
    """,
    openapi_tags=openapi_tags,
    summary="Smart beacons API",
    swagger_ui_parameters={
        "deepLinking": False,
        # "defaultModelRendering": "model",
        "operationsSorter": "alpha",
        "syntaxHighlight": True,
    },
    version="0.1.0",
)

# ---------------------------------------------------------
# user specific EPs (1st Ports)
# ---------------------------------------------------------
# TODO: fix appearance order in Swagger documentation

for port in ACTIVE_PORTS:
    prefix = "/".join(["", "beacons", port.__name__.split(".")[-1]])
    app.include_router(port.router, prefix=prefix)
    print(f"Activating: {port.__name__}")

# old router adding fashion
# app.include_router(search.router)
# app.include_router(stats.router)
# app.include_router(config.router)

# ---------------------------------------------------------
# Middleware settings
# ---------------------------------------------------------
app.add_middleware(GZipMiddleware, minimum_size=500)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO def for prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ---------------------------------------------------------
# Static assets
# ---------------------------------------------------------
for path in loader.find(type_="d", name="static"):
    name = os.path.basename(path)
    app.mount(f"/{name}", StaticFiles(directory=path), name=name)
    break


# ---------------------------------------------------------
# heartbeat EP
# ---------------------------------------------------------
@app.get("/")
async def root():
    return {"message": "Hello World!!"}


# ---------------------------------------------------------
# direct execution case (python -m xxxx)
# (not used by now)
# ---------------------------------------------------------
if __name__ == "__main__":
    """
    $ uvicorn beacons.beacons:app --reload --reload-delay 1 --reload-dir ~/your/code/beacons --reload-exclude 'venv' --loop uvloop
    """

    uvicorn.run(app, host="0.0.0.0", port=8009)
