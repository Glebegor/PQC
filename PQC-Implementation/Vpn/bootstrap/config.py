import json
import os

class Config:
    def __init__(self, config_path="./config.json"):
        self.config_path = config_path
        self.config_data = self._load_config()

    def _load_config(self):
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
        with open(self.config_path, "r") as file:
            return json.load(file)

    def get(self, key, default=None):
        return self.config_data.get(key, default)