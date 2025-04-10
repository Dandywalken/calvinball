from typing import Type

from dcs.helicopters import HelicopterType, helicopter_map
from dcs.planes import PlaneType, plane_map
from dcs.unittype import VehicleType, ShipType, StaticType
from dcs.vehicles import vehicle_map
from dcs.ships import ship_map
from dcs.statics import cargo_map, fortification_map


def helicoptermod(helicopter: Type[HelicopterType]) -> Type[HelicopterType]:
    helicopter_map[helicopter.id] = helicopter
    return helicopter


def planemod(plane: Type[PlaneType]) -> Type[PlaneType]:
    plane_map[plane.id] = plane
    return plane


def vehiclemod(vehicle: Type[VehicleType]) -> Type[VehicleType]:
    vehicle_map[vehicle.id] = vehicle
    return vehicle


def shipmod(ship: Type[ShipType]) -> Type[ShipType]:
    ship_map[ship.id] = ship
    return ship


def cargomod(static: Type[StaticType]) -> Type[StaticType]:
    cargo_map[static.id] = static
    return static


def fortificationmod(static: Type[StaticType]) -> Type[StaticType]:
    fortification_map[static.id] = static
    return static