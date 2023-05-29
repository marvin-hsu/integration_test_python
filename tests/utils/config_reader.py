import os

import toml


class Config:
    def __init__(self, env):
        self.config = None
        self.env = env
        self.load_config()

    def load_config(self):
        config_directory = os.path.join(os.path.dirname(os.getcwd()), "configurations")
        config_path = None

        if self.env == "qa":
            config_path = os.path.join(config_directory, "qa.toml")

        elif self.env == "local":
            config_path = os.path.join(config_directory, "local.toml")

        with open(config_path, "r") as f:
            config_data = toml.load(f)

        # 將config_data轉換為config物件
        self.config = ConfigObject(config_data)


class ConfigObject:
    def __init__(self, config_data):
        self
