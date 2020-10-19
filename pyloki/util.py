import os
from collections import defaultdict
class Namespace:
    pass
def reverse_dictionary(oDict):
    #nDict = type(oDict)()
    nDict = defaultdict(list)
    for key, value_sequence in oDict.items():
        for value in value_sequence:
            nDict[value].append(key)
    return nDict
def get_username( prompt='username:', var=None ):
    return (var and os.environ.get(var,None)) or input(prompt)
def get_password( prompt='password:', var=None ):
    return (var and os.environ.get(var,None)) or getpass.getpass(prompt)
def lmap(f,seq):
    return list(map(f,seq))

class UniqExc(Exception): pass
class UniqTooFew(UniqExc): pass
class UniqTooMany(UniqExc): pass
def unique(oSeq):
    oList = list(oSeq)
    if   len(oList) > 1: raise UniqTooMany
    elif len(oList) < 1: raise UniqTooFew
    else: return oList[0]
