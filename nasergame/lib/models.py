from functools import lru_cache

import importlib.resources

import nasergame.models
from nasergame.lib.objmodel import Model


@lru_cache(maxsize=None)
def load(name):
    model_text = importlib.resources.read_text(nasergame.models, f"{name}.obj")
    polylines = Model(model_text)
    return polylines
