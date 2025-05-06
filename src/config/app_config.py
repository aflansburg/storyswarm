import os
import uuid
import yaml
from .logger import get_default_logger


log = get_default_logger()


class AppConfig:
    """
    Singleton class for storing application configuration.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.uid = str(uuid.uuid4())
            log.debug(f"Created AppConfig instance with UID: {cls._instance.uid}")
        return cls._instance

    def __load_config(self):
        """
        Load the config from the environment variables and
        ensure all required env var are present.

        :param self: The AppConfig instance.
        :param ensure: Whether to ensure all required env vars are present.
            Defaults to True.
        :return: None
        """
        with open("./src/config/environment.yaml", "r") as environment_file:
            environment_config = yaml.safe_load(environment_file)

        with open("./src/config/defaults.yaml", "r") as defaults_file:
            defaults_config = yaml.safe_load(defaults_file)

        for env_var in environment_config["required_env_vars"]:
            if env_var not in os.environ:
                log.error(f"Environment variable {env_var} is not set.")
                raise ValueError(f"Environment variable {env_var} is not set.")
            self.__dict__[env_var] = os.environ[env_var]

        for key, value in defaults_config.items():
            if key not in self.__dict__["defaults"]:
                self.__dict__["defaults"][key] = value

        # Set some defaults
        self.PORT = os.environ.get("PORT", 8080)
        self.LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
        self.uid = self.__dict__["uid"]

    def __init__(self):
        self.__dict__["_frozen"] = False
        self.__dict__["defaults"] = {}
        self.__load_config()
        self.__dict__["_frozen"] = True

    def __setattr__(self, key, value):
        if getattr(self, "_frozen", False):
            raise AttributeError(
                f"Cannot modify frozen AppConfig instance {self.uid}. Attempted to set {key} to {value}."
            )
        super().__setattr__(key, value)
