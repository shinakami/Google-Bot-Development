import webot as we
import os
import numpy as np
print("Running this ApiTest")

minimum = 5

portlist = we.IPmoder()["Port"].array
portarray = portlist.to_numpy()
portmax = np.max(portarray)
print(portmax)

listValidIP = we.SSLIPcatcher(minimum_ipcount=minimum)

#we.Exacute(ActIps=listValidIP)

print(listValidIP)

listLenofValidIP = len(listValidIP)
overnum = 50


def test_Maxmimum():
    assert  int(portmax) > 90000

def test_overnum():
    assert overnum == 50

def test_num():
    assert minimum == 5

def test_isNotNull():
    assert listValidIP

def test_qualify():
    assert listLenofValidIP > minimum or listLenofValidIP > overnum





os.system("pause")