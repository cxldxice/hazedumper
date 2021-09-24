#name: hazedumper
#desc: pkg for auto update offsets
#source: https://github.com/frk1/hazedumper
#author: by @fxcvd

import requests

from .default import *


HAZEDUMPER_URL = "https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.min.json"
LoadError = Exception("LoadError")


def load():
    res = requests.get(HAZEDUMPER_URL)

    if res.status_code != 200:
        raise LoadError

    json = res.json()
    offsets = dict(json["signatures"].items() | json["netvars"].items())

    for offset in offsets:
        globals()[offset] = offsets[offset]


if __name__ != "__main__":
    load()