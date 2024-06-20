import socket
import requests
from ..scripts import Scripted
#====================================================================

class InterNet:

    def GetIP():
        moones = requests.get(Scripted.DATA01)
        moonus = moones.json()
        return moonus['ip']

#====================================================================

    def GetLIP():
        moones = socket.gethostname()
        moonus = socket.gethostbyname(moones)
        return moonus

#====================================================================
