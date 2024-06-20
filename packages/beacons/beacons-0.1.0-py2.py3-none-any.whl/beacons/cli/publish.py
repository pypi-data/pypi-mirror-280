# import re
# import os
# import yaml

import click

from swarmtube.logic.swarmtube import App, SurrealBroker, Subscription
from syncmodels.storage import SurrealistStorage, WaveStorage

from .main import *
from .config import *
from ..logic.beacons import BeaconsTracesOrionSync
from ..definitions import (
    BEACONS_TRACE_THING,
    BEACONS_TRACE_NS,
    BEACONS_TRACE_DB,
    BEACONS_ORION_TUBE,
)


@main.group(context_settings=CONTEXT_SETTINGS)
@click.pass_obj
def publish(env):
    """subcommands for managing workspaces for beacons"""
    # banner("User", env.__dict__)
    pass


@publish.command()
@click.option("--path", default=None)
@click.pass_obj
def traces(env, path):
    """Publish beacon traces into platform"""
    # force config loading
    config.callback()

    url = env.surreal_url
    broker = SurrealBroker(url)
    surreal = SurrealistStorage(url)
    storage = WaveStorage(storage=surreal)
    ctx = dict(storage=storage, broker=broker)

    traces = f"{BEACONS_TRACE_NS}://{BEACONS_TRACE_DB}/{BEACONS_TRACE_THING}"
    sources = [traces]
    target = f"{BEACONS_TRACE_NS}://{BEACONS_TRACE_DB}/{BEACONS_ORION_TUBE}"

    particle = BeaconsTracesOrionSync(target, sources, **ctx)

    app = App(**ctx)
    app.add(particle)
    app.run()
