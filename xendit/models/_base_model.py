import json
from dataclasses import dataclass


@dataclass(init=False)
class BaseModel(dict):
    """Abstract class for feature class. Useful for pretty print and automatically set attribute"""

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return json.dumps(vars(self), indent=4)

    def initialize_dict(self, **kwargs):
        dict_params = {}
        for key, value in kwargs.items():
            if value is not None:
                dict_params[key] = value
        dict.__init__(self, dict_params)