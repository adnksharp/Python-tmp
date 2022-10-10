import numpy as np
from math import sin as s
from math import cos as c
from numpy import pi as pi
import math as mth
#rotacion
def Rx(arg):
    R=np.array([[1,0,0,0],
               [0,c(arg),-s(arg),0],
                [0, s(arg),c(arg),0],
                [0,0,0,1]])
    return R


def Rz(arg):
    R=np.array([[c(arg),-s(arg),0,0],
                [s(arg),c(arg),0,0],
                 [0,0,1,0],
                [0,0,0,1]])
    return R
def Ry (arg):
    R=np.array([[c(arg),0,s(arg),0],
                [0, 1,0,0],
               [-s(arg),0,c(arg),0],
                [0,0,0,1]])
    return R
#traslacion

def Tx (arg):
    T=np.identity(4)
    T[0,3]=arg
    return T
def Ty (arg):
    T=np.identity(4)
    T[1,3]=arg
    return T
def Tz (arg):
    T=np.identity(4)
    T[2,3]=arg
    return T



