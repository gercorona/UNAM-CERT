#!/usr/bin/env python

from random import *
minus = "abcdefghijklmnopqrstuvwxyz"
mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digitos = "1234567890"


def genera_contra(minuscula,may,dig):
    if minuscula > 0:
        if may > 0:
            if dig > 0:
                return choice(minus) + choice(may) + choice(dig) + genera_contra(minuscula-1,may-1,dig-1)
            else:
                return choice(minus) + choice(may) + genera_contra(minuscula-1,may-1,0)
        else:
            if dig > 0:
                return choice(minus) + choice(dig) + genera_contra(minuscula-1,0,dig-1)
            else:
                return choice(minus) + choice(may) + genera_contra(minuscula-1,0,0)
            
    else: 
        if may > 0:
            if dig > 0:
                return choice(minus) + choice(may) + choice(dig) + genera_contra(minuscula-1,may-1,dig-1)
            else:
                return choice(minus) + choice(may) + genera_contra(minuscula-1,may-1,0)
        else:
            if dig > 0:
                return choice(minus) + choice(dig) + genera_contra(minuscula-1,0,dig-1)
            else:
                return choice(minus) + choice(may) + genera_contra(minuscula-1,0,0)


passwd = genera_contra(3,5,2)

print passwd