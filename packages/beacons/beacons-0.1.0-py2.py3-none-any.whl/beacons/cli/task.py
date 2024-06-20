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

# Import local inventory models
from beacons.models.task import BeaconsTask as Item
from beacons.models.task import BeaconsTaskRequest as Request
from beacons.models.task import BeaconsTaskResponse as Response

# ---------------------------------------------------------
# Dynamic Loading Interface / EP Exposure
# ---------------------------------------------------------
TAG = "Tasks"
DESCRIPTION = "Tasks CLI API"
API_ORDER = 10

# ---------------------------------------------------------
# Loggers
# ---------------------------------------------------------

from agptools.logs import logger

log = logger(__name__)

# ---------------------------------------------------------
# Task CLI port implementation
# ---------------------------------------------------------
@main.group(context_settings=CONTEXT_SETTINGS)
@click.pass_obj
def task(env):
    """subcommands for managing tasks for beacons"""
    # banner("User", env.__dict__)


submodule = task


@submodule.command()
@click.option("--path", default=None)
@click.pass_obj
def create(env, path):
    """Create a new task for beacons"""
    # force config loading
    config.callback()

    # TODO: implement


@submodule.command()
@click.pass_obj
def read(env):
    """Find and list existing tasks for beacons"""
    # force config loading
    config.callback()

    # TODO: implement


@submodule.command()
@click.pass_obj
def update(env):
    """Update and existing task for beacons"""
    # force config loading
    config.callback()

    # TODO: implement


@submodule.command()
@click.pass_obj
def delete(env):
    """Delete an existing task for beacons"""
    # force config loading
    config.callback()

    # TODO: implement
