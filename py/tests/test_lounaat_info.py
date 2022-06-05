import lounaat_info as subject


def test_version():
    assert subject.__version__ == '0.1.0', "__version__ mismatch"


def test_env_is_read():
    assert subject.ENV is not None, "ENV is None"
    assert isinstance(subject.ENV, dict), "ENV is not a dict"


def test_env_discord_webhook():
    discord = subject.ENV["DISCORD_WEBHOOK"]
    assert discord, "Missing from env: DISCORD_WEBHOOK"
    assert discord != "", "DISCORD_WEBHOOK is empty"
