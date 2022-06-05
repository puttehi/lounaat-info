from typing import Dict, List
from bs4 import BeautifulSoup
import lounaat_info.parse as subject

from tests.test_fetch import MockResponse
from lounaat_info.custom_types import DishData, ParsedResponse, RestaurantData


def test_parse_does_not_throw():
    res = MockResponse()
    subject.parse(res.text, 0, 0, 0)


def test_parse_returns_expected_dict_keys():

    expected: ParsedResponse = {
        "restaurants": [{"key": "value"}],
        "lat": str(),
        "lon": str(),
        "weekday": int(),
    }

    res = MockResponse()
    actual = subject.parse(res.text, 0, 0.1, 0.1)

    actual_keys = actual.keys()
    expected_keys = expected.keys()

    for key in expected_keys:
        assert key in actual_keys


def test_parse_returns_expected_shallow_types():

    expected: ParsedResponse = {
        "restaurants": [{"key": "value"}],
        "lat": str(),
        "lon": str(),
        "weekday": int(),
    }

    res = MockResponse()
    actual = subject.parse(res.text, 0, 0, 1)

    actual_items = actual.items()

    for k, v in actual_items:
        assert type(v) == type(expected[k])


def test_parse_restaurants_returns_expected_data():

    expected: List[RestaurantData] = [
        {
            "href": "/lounas/kainuun-portti/kajaani",
            "name": "Kainuun Portti",
            "dishes": [
                {"name": "Hernekeittoa", "info": ""},
                {"name": "Sipuliset pannupihvit", "info": ""},
                {"name": "Muusia & pannukakkua", "info": ""},
            ],
            "lunch_time": "10:30-14:30",
        },
        {
            "href": "/lounas/amica-atima/kajaani",
            "name": "Amica Atima",
            "dishes": [],
            "lunch_time": "10:30-13",
        },
        {
            "href": "/lounas/pancho-villa-kajaani/kajaani",
            "name": "Pancho Villa Kajaani",
            "dishes": [],
            "lunch_time": "10:30-14",
        },
        {
            "href": "/lounas/lori/kajaani",
            "name": "Lori",
            "dishes": [],
            "lunch_time": "11-15",
        },
    ]

    res = MockResponse()
    actual = subject.parse_restaurants(res.text)

    assert actual == expected


def test_parse_dishes_returns_expected_data():

    expected: List[DishData] = [
        {"name": "Hernekeittoa", "info": ""},
        {"name": "Sipuliset pannupihvit", "info": ""},
        {"name": "Muusia & pannukakkua", "info": ""},
    ]

    input = '<div class="menu item category-0"><div class="item-header"><div class="icon"><a href="#4313" class="favorite dislike" title="lisää/poista suosikeista"></a></div> <h3><a href="/lounas/kainuun-portti/kajaani">Kainuun Portti</a></h3><div class="details"><ul class="review"><li class="current" style="width: 0%;">/5.0</li></ul><div class="icon-s"><a href="#4313" class="hide" title="älä näytä tätä ravintolaa enää"></a></div><p class="lunch closed"><i class="fa fa-clock-o"></i> 10:30-14:30</p></div></div><div class="item-body"><ul><li class="menu-item item-diet-l item-diet-g"><p class="dish">Hernekeittoa   <a href="#g" title="Gluteeniton" class="diet diet-g">g </a>     <a href="#l" title="Laktoositon" class="diet diet-l">l  </a> </p></li><li class="menu-item item-diet-l item-diet-g"><p class="dish">Sipuliset pannupihvit   <a href="#g" title="Gluteeniton" class="diet diet-g">g </a>     <a href="#l" title="Laktoositon" class="diet diet-l">l  </a> </p></li><li class="menu-item"><p class="dish">Muusia & pannukakkua</p></li></ul></div><div class="item-footer"><p class="dist" title="Mainuantie 350, 87700 Kajaani"><i class="fa fa-map-marker"></i> 0m</p></div></div>'

    soup = BeautifulSoup(input, features="html.parser")

    actual = subject.parse_dishes(soup.select_one("div.menu.item"))

    assert actual == expected
