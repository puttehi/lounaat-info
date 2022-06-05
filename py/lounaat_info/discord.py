import json
import requests
from typing import Any, List, TypedDict

from .custom_types import ParsedResponse, RestaurantData


class FieldData(TypedDict):
    name: str
    value: str


class EmbedData(TypedDict):
    title: str
    description: str
    url: str
    color: int
    fields: List[FieldData]


class DiscordWebhookMessage(TypedDict):
    content: str
    embeds: List[EmbedData]
    attachments: List[Any]


def transform_to_discord_message_with_embeds(
    date: str, data: ParsedResponse
) -> DiscordWebhookMessage:
    msg: DiscordWebhookMessage = {}

    msg[
        "content"
    ] = f"Kajaani Lunch for {date} - Source: [lounaat.info](https://www.lounaat.info)"
    msg["embeds"] = []

    restaurant_datas = data["restaurants"]

    for r in restaurant_datas:
        embed: EmbedData = {}
        embed["title"] = f"{r['name']} - {r['lunch_time']}"
        embed["description"] = f"[Map link (xxx m)](https://www.google.fi)"  # TODO
        embed["url"] = f"https://www.lounaat.info{r['href']}"
        embed["color"] = 16777215
        embed["fields"] = []

        for d in r["dishes"]:
            field: FieldData = {
                "name": f":canned_food: {d['name']}",
                "value": f":information_source: {d['info']}",
            }
            embed["fields"].append(field)
            print(field)

        msg["embeds"].append(embed)

    # Discord maxes embeds at 10
    msg["embeds"] = msg["embeds"][0:9]

    msg["attachments"] = []

    return msg


def call_webhook(msg: DiscordWebhookMessage, webhook_url: str) -> None:

    try:
        response = requests.post(
            webhook_url,
            data=json.dumps(msg),
            headers={"Content-Type": "application/json"},
        )
    except Exception as e:
        print(e)
        print("Message was")
        print(msg)
        raise (e)

    print(response.text)
    print(f"Sent message: {msg}")


# {
#   "content": "Kajaani Lunch for {date}  - Source: [lounaat.info](https://www.lounaat.info)",
#   "embeds": [
#     {
#       "title": "{restaurant_1} - {lunch_time}",
#       "description": "[{distance}]({map_link})",
#       "url": "{restaurant_url}",
#       "color": 16777215,
#       "fields": [
#         {
#           "name": "{dish}",
#           "value": "{info}"
#         },
#         {
#           "name": "{dish}",
#           "value": "{info}"
#         },
#         {
#           "name": "{dish}",
#           "value": "{info}"
#         },
#         {
#           "name": "{dish}",
#           "value": "{info}"
#         },
#         {
#           "name": "{dish}",
#           "value": "{info}"
#         }
#       ]
#     },
#     {
#       "title": "{restaurant_2} - {lunch_time}",
#       "description": "[{distance}]({map_link})",
#       "url": "{restaurant_url}",
#       "color": 16777215,
#       "fields": [
#         {
#           "name": "{dish}",
#           "value": "{info}"
#         },
#         {
#           "name": "{dish}",
#           "value": "{info}"
#         },
#         {
#           "name": "{dish}",
#           "value": "{info}"
#         },
#         {
#           "name": "{dish}",
#           "value": "{info}"
#         },
#         {
#           "name": "{dish}",
#           "value": "{info}"
#         }
#       ]
#     }
#   ],
#   "attachments": []
# }
