from typing import Tuple, Type

import pkg_resources
from trinity.components.eth2.beacon_trio.component import (
    BeaconNodeComponent as TrioBeaconNodeComponent,
)
from trinity.components.eth2.discv5.component import DiscV5Component
from trinity.components.eth2.network_generator.component import (
    NetworkGeneratorComponent,
)
from trinity.extensibility import BaseComponentAPI

BEACON_NODE_COMPONENTS: Tuple[Type[BaseComponentAPI], ...] = (
    NetworkGeneratorComponent,
    DiscV5Component,
)


def discover_components() -> Tuple[Type[BaseComponentAPI], ...]:
    # Components need to define entrypoints at 'trinity-eth2.components' to automatically get loaded
    # https://packaging.python.org/guides/creating-and-discovering-components/#using-package-metadata

    return tuple(
        entry_point.load()
        for entry_point in pkg_resources.iter_entry_points("trinity-eth2.components")
    )


def get_all_components(
    *extra_components: Type[BaseComponentAPI],
) -> Tuple[Type[BaseComponentAPI], ...]:
    return extra_components + discover_components()


def get_components_for_beacon_client() -> Tuple[Type[BaseComponentAPI], ...]:
    return BEACON_NODE_COMPONENTS


def get_components_for_trio_beacon_client() -> Tuple[Type[BaseComponentAPI], ...]:
    return (
        TrioBeaconNodeComponent,
        # NOTE: we import this just for the cli parsing...
        # TODO: pull cli options into beacon node when we merge these components
        DiscV5Component,
        NetworkGeneratorComponent,
    )
