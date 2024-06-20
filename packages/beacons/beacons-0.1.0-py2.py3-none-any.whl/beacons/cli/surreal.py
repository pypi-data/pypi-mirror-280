# import asyncio
# import random
import time
import click

from agptools.helpers import parse_uri
from agptools.logs import logger

# from bigplanner.definitions import DEFAULT_LANGUAGE, UID_TYPE

# TODO: include any logic from module core
# Examples
# from bigplanner.models import *
# from bigplanner.logic import Tagger
# from syncmodels.storage import Storage

# Import local inventory models
# from bigplanner.models.task import PlannerTask as Item
# from bigplanner.models.task import PlannerTaskRequest as Request
# from bigplanner.models.task import PlannerTaskResponse as Response

from syncmodels.helpers.surreal import SurrealServer
from syncmodels.helpers.faker import fake

from surrealist import Surreal

# from bigplanner.helpers import *
from beacons.cli.main import main, CONTEXT_SETTINGS
from beacons.cli.config import config

# ---------------------------------------------------------
# Dynamic Loading Interface / EP Exposure
# ---------------------------------------------------------
TAG = "SURREAL"
DESCRIPTION = "SurrealDB CLI API"
API_ORDER = 10

# ---------------------------------------------------------
# Loggers
# ---------------------------------------------------------

log = logger(__name__)


# ---------------------------------------------------------
# Task CLI port implementation
# ---------------------------------------------------------
@main.group(context_settings=CONTEXT_SETTINGS)
@click.pass_obj
def surreal(env):
    """subcommands for manage tasks for bigplanner"""
    # banner("User", env.__dict__)


submodule = surreal


@submodule.command()
@click.option("--path", default=None)
@click.pass_obj
def start(env, path):
    """Start Surreal Server"""
    # force config loading
    config.callback()

    db_path = env.db_url
    surreal_url = env.surreal_url
    uri = parse_uri(surreal_url)
    bind = "0.0.0.0:{port}".format_map(uri)
    server = SurrealServer(path=db_path, bind=bind, daemon=True)
    if server.start():
        log.info("Surreal Server running: %s : %s", bind, db_path)
        log.info("User `ine surreal stop` for stopping server")
    else:
        log.error("Launching Surreal server FAILED: %s : %s", bind, db_path)


@submodule.command()
@click.pass_obj
def stop(env):
    """Stop Surreal Server"""
    # force config loading
    config.callback()

    db_path = env.db_url
    surreal_url = env.surreal_url
    uri = parse_uri(surreal_url)
    bind = "0.0.0.0:{port}".format_map(uri)
    server = SurrealServer(path=db_path, bind=bind, daemon=True)
    if server.stop():
        log.info("Surreal Server stopped: %s : %s", bind, db_path)
    else:
        log.info("Unable to Stop Server: %s : %s", bind, db_path)



