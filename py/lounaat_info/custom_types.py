from typing import Any, List, Dict, OrderedDict, TypedDict, Union, Tuple


class DishData(TypedDict):
    name: str
    info: str


class RestaurantData(TypedDict):
    name: str
    href: str
    dishes: List[DishData]
    lunch_time: str


class ParsedResponse(TypedDict):
    restaurants: List[RestaurantData]
    lat: str
    lon: str
    weekday: int
