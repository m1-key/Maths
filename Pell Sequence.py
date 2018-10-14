# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 23:03:27 2018

@author: Mithilesh
"""

def pell(n):
    a,b=0,1
    for i in range(n):
        print(b,end=" , ")
        a,b=b,2*b+a     #Pell's Sequence is defined as P(n)=2P(n-1)+P(n-2)
    print(" . . . . . . . . ")
n=int(input("Enter the number : "))
pell(n)