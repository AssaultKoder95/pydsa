"""
Lowest Common Multiple
----------------------

A very simple implementation of LCM

Pseudo Code: https://en.wikipedia.org/wiki/Least_common_multiple
"""


def lcm(a, b):

    temp = a
    while (temp % b) != 0:
        temp += a
    return temp

