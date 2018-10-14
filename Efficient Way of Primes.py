# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 00:55:29 2018

@author: Mithilesh
"""

def Sieve_of_Eratosthenes(n):
    prime=[True for i in range(n+1)]  #Boolean Array
    num=2
    while ((num**2)<=n):
        if prime[num]==True:
            for j in range(2*num,n+1,num):   
                prime[j]=False               #Removing Multiples as they are not prime
        num+=1
    
    for k in range(2,n+1):       #Printing array elements whose value is True,i.e they are prime.
        if prime[k]==True:
            print(k,end=" , ")

n=int(input("Enter the number : "))
Sieve_of_Eratosthenes(n)