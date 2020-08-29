# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 13:56:56 2020

@author: VVincent
"""


#startNumber = 2000
#endNumber = 3200
startNumber = int(input("Provide the starting number: "))
endNumber = int(input("Provide the ending number: "))
listNumber = []
stringNumbers=""
for i in range(startNumber, endNumber+1):
    if(i%7==0 and i%5!=0):
        listNumber.append(i)
        if stringNumbers=='':
            stringNumbers = stringNumbers+str(i)
        else:
            stringNumbers = stringNumbers+','+str(i)


# print in single line
print(stringNumbers)