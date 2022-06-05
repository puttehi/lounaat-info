import lounaat_info as lounaat_info

def test_version():
    assert lounaat_info.__version__ == '0.1.0', "__version__ mismatch"


def test_env_is_read():
    assert lounaat_info.ENV is not None, "ENV is None"
    assert isinstance(lounaat_info.ENV, dict), "ENV is not a dict"


def test_env_discord_webhook():
    discord = lounaat_info.ENV["DISCORD_WEBHOOK"]
    assert discord, "Missing from env: DISCORD_WEBHOOK"
    assert discord != "", "DISCORD_WEBHOOK is empty"
