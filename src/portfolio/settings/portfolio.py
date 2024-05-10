import os
from collections import namedtuple

from environment import env


Env = namedtuple(typename="Env", field_names=["DEV", "PROD", "LOCAL"])(*["dev", "prod", "local"])

ENV_NAME = os.environ.get("ENV_NAME", "local")
