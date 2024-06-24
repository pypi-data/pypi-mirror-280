import json
import socket
import requests
from ..scripts import Apis
#================================================================

class InterNet:

    def GetIP():
        moones = requests.get(Apis.DATA02)
        moonus = moones.json()
        return moonus['ip']

    def GetLIP():
        moones = socket.gethostname()
        moonus = socket.gethostbyname(moones)
        return moonus

    def tracker(IP):
        mainse = requests.get(Apis.DATA01.format(IP))
        moonus = json.loads(mainse.text)
        return moonus

#================================================================
