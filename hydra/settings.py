import os.path
import pathlib

import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = os.path.join(BASE_DIR, "etc", "hydra.yml")


def get_settings(path):
    with open(path) as f:
        return yaml.load(f)


settings = get_settings(config_path)
