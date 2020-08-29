# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 15:00:06 2020

@author: VVincent
"""

#Python program to calcualte the volume of sphere with formula V=4/3 * pi * r^3

import math

def getVolume():
    return lambda r:(4/3)*round(math.pi, 3)*r*r*r

sphereDia = float(input("Enter diameter: "))

volume=getVolume()

print("Volume: ", round(volume(sphereDia), 3))

