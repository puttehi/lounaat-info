from typing import List
from .custom_types import DishData, ParsedResponse, RestaurantData
from bs4 import BeautifulSoup
from bs4.element import Tag


def parse(text: str, day: int, lat: float, lon: float) -> ParsedResponse:

    parsed: ParsedResponse = {
        "restaurants": [{}],
        "lat": str(lat),
        "lon": str(lon),
        "weekday": int(day),
    }

    parsed["restaurants"] = parse_restaurants(text)

    return parsed


def parse_restaurants(text: str) -> List[RestaurantData]:

    parsed: List[RestaurantData] = []

    soup = BeautifulSoup(text, features="html.parser")

    restaurant_divs = soup.select("div.menu.item")
    for div in restaurant_divs:
        h = div.find("h3")
        name = h.a.text
        href = h.a.get("href")

        clock_element = div.find("p", class_="lunch")
        lunch_time = clock_element.text.strip()

        parsed.append(
            {
                "name": name,
                "href": href,
                "dishes": parse_dishes(div),
                "lunch_time": lunch_time,
            }
        )

    return parsed


def parse_dishes(div: Tag) -> List[DishData]:

    parsed: List[DishData] = []

    dishes = div.select("p.dish")

    for d in dishes:
        name = d.contents[0].strip()  # Removes allergens
        info = ""  # TODO
        parsed.append({"name": name, "info": info})

    return parsed
