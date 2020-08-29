# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 14:26:19 2020

@author: VVincent
"""


firstName = input("First Name: ")
lastName = input("Last Name:")

#fullName = firstName.lower() + ' ' + lastName.lower()
fullName = firstName.strip() + ' ' + lastName.strip()

print(fullName[::-1])