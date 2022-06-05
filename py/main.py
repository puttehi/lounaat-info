from lounaat_info.discord import transform_to_discord_message_with_embeds, call_webhook
from lounaat_info.fetch import fetch_lunch_data
from lounaat_info.parse import parse
from lounaat_info import ENV

if __name__ == "__main__":

    day = 8 # 0 = sunday : 6 = saturday -> Higher numbers go back in history
    lat = 64.24803849999999
    lon = 27.7996717
    res = fetch_lunch_data(day, lat, lon)
    data = parse(res.text, day, lat, lon)
    msg = transform_to_discord_message_with_embeds("date_string", data)
    call_webhook(msg, ENV["DISCORD_WEBHOOK"])
