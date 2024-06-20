# import re
# import os
# import yaml

import click

# from beacons.helpers import *
from beacons.cli.main import main, CONTEXT_SETTINGS
from beacons.cli.config import config

from beacons.definitions import DEFAULT_LANGUAGE, UID_TYPE

# TODO: include any logic from module core
# Examples
# from beacons.models import *
# from beacons.logic import Tagger
# from syncmodels.storage import Storage

# Import local scripts models
from beacons.models.script import BeaconsScript as Item
from beacons.models.script import BeaconsScriptRequest as Request
from beacons.models.script import BeaconsScriptResponse as Response

# ---------------------------------------------------------
# Dynamic Loading Interface / EP Exposure
# ---------------------------------------------------------
TAG = "Scripts"
DESCRIPTION = "Scripts CLI API"
API_ORDER = 10

# ---------------------------------------------------------
# Loggers
# ---------------------------------------------------------

from agptools.logs import logger

log = logger(__name__)

# ---------------------------------------------------------
# Script CLI port implementation
# ---------------------------------------------------------
@main.group(context_settings=CONTEXT_SETTINGS)
@click.pass_obj
def script(env):
    """subcommands for managing scripts for beacons"""
    # banner("User", env.__dict__)


submodule = script


@submodule.command()
@click.option("--path", default=None)
@click.pass_obj
def create(env, path):
    """Create a new script for beacons"""
    # force config loading
    config.callback()

    # TODO: implement


@submodule.command()
@click.pass_obj
def read(env):
    """Find and list existing scripts for beacons"""
    # force config loading
    config.callback()

    # TODO: implement


@submodule.command()
@click.pass_obj
def update(env):
    """Update and existing scripts for beacons"""
    # force config loading
    config.callback()

    # TODO: implement


@submodule.command()
@click.pass_obj
def delete(env):
    """Delete an existing scripts for beacons"""
    # force config loading
    config.callback()

    # TODO: implement
