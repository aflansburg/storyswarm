import pytest
from config.app_config import AppConfig


def test_app_config_is_frozen(monkeypatch):
    monkeypatch.setenv("DUMMY_ENV_VAR", "dummy_value")
    monkeypatch.setenv("PORT", "1234")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")

    import yaml

    monkeypatch.setattr(
        yaml, "safe_load", side_effect := lambda f: next(side_effect.values)
    )
    side_effect.values = iter(
        [
            {"required_env_vars": ["DUMMY_ENV_VAR"]},  # for environment.yaml
            {},  # for defaults.yaml
        ]
    )

    from unittest.mock import mock_open

    monkeypatch.setattr("builtins.open", mock_open(read_data="{}"))

    config = AppConfig()

    with pytest.raises(AttributeError, match="Cannot modify frozen AppConfig instance"):
        config.NEW_ATTRIBUTE = "should fail"

    with pytest.raises(AttributeError, match="Cannot modify frozen AppConfig instance"):
        config.PORT = 9999

    # reading should still work
    assert config.PORT == "1234"
    assert config.LOG_LEVEL == "DEBUG"
