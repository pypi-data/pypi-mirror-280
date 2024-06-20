import asyncio

# import re
import os
import yaml

import click
from pprint import pp
from agptools.files import fileiter

from syncmodels.helpers.importers import ExcelImporter
from syncmodels.storage import DualStorage

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
from beacons.models.inventory import BeaconInventoryItem as Item
from beacons.models.inventory import BeaconsInventory as Inventory

# from beacons.models.inventory import BeaconsInventoryRequest as Request
# from beacons.models.inventory import BeaconsInventoryResponse as Response
from beacons import mappers

# ---------------------------------------------------------
# Dynamic Loading Interface / EP Exposure
# ---------------------------------------------------------
TAG = "Inventory"
DESCRIPTION = "Inventory CLI API"
API_ORDER = 10

# ---------------------------------------------------------
# Loggers
# ---------------------------------------------------------

from agptools.logs import logger

log = logger(__name__)


# ---------------------------------------------------------
# Inventory CLI router
# ---------------------------------------------------------
@main.group(context_settings=CONTEXT_SETTINGS)
@click.pass_obj
def inventory(env):
    """subcommands for managing inventory for beacons"""
    # banner("User", env.__dict__)


submodule = inventory


@submodule.command()
@click.option("--path", default=None)
@click.option("--pattern", default=None)
@click.pass_obj
def create(env, path, pattern):
    """Create a new inventory item for beacons (TBD)"""
    # force config loading
    config.callback()

    # TODO: implement


@submodule.command()
@click.pass_obj
def read(env):
    """Find and list existing inventory items for beacons"""
    # force config loading
    config.callback()

    async def main():
        storage = DualStorage()
        table = "inventory"
        data = await storage.get(table)
        inventory = Inventory(**data)
        print(f"{inventory.id}: {len(inventory.item)} items")

    asyncio.run(main())


@submodule.command()
@click.option("--path", multiple=True, default=["."])
@click.option(
    "--pattern",
    multiple=True,
    default=[r"(?P<name>.*)(?P<ext>\.(csv|xls|xlsx))$"],
)
# @click.option("--pattern", multiple=True, default=[r"*.xlsx"])
@click.pass_obj
def update(env, path, pattern):
    """Update and existing inventory item from csv, xls files.

    IBKS4AA00088892

    """
    # force config loading
    config.callback()

    async def main():

        # IDX = set(['ID Beakon', 'Case Serial'])
        # r"[0-9A-F]{32}"
        # r"IBKS(\w){11}"]
        db = ExcelImporter.load(
            file_pattern=pattern, value_pattern=[r"(IBKS|IKBS)(\w){11}"]
        )
        # TODO: remove, just for debuging
        yaml.dump(
            db,
            stream=open("inventory.debug.yaml", "w", encoding="utf-8"),
            Dumper=yaml.Dumper,
        )

        inventory = Inventory(id="inventory")
        # inventory = Inventory()
        for uid, data in db.items():
            try:
                item = mappers.inventory.BeaconItem.pydantic(data)
                # print(item)
                assert isinstance(item, Item)
                if item.id.startswith('42'):
                    inventory.item[item.id] = item
            except Exception as why:
                pp(data)
                print(f"Validation Error for: {data}: {why}")
                foo = 1

        print(f"[{len(inventory.item)}] valid beacons")
        storage = DualStorage()
        data = inventory.model_dump()
        table = "inventory"
        await storage.set(table, data)
        await storage.save(wait=True)

        # test ="IBKS10500" & F131
        # kk = await storage.get(table)
        # foo = 1

    asyncio.run(main())
    # yaml.dump(data, stream=open("inventory.yaml", "w", encoding="utf-8"), Dumper=yaml.Dumper)


@submodule.command()
@click.pass_obj
def delete(env):
    """Delete an existing inventory item for beacons"""
    # force config loading
    config.callback()

    # TODO: implement
