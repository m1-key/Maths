# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 14:43:34 2018

@author: Mithilesh
"""
import math
def LEFT_TRUNCATABLE_PRIMES(n):
    temp=n
    sum1,flag=0,0
    temp2=str(n)
    lst=[0,1,2,4,5,6,8,9]
    var=int(temp2[-1])
    if var in lst:
        sum1=0
    else:
        for i in range(len(str(n))):
            for j in range(2,int(math.sqrt(temp))):
                if temp%j==0:
                    flag=1
                    break
                else:
                    continue
            if flag==1:
                break
            else:
                sum1+=1
                if len(str(temp))>2:
                    temp2=str(temp)
                    temp=int(temp2[1:])
                else:
                    break
    if sum1==len(str(n))-1:
        print("YES")
    else:
        print("NO")

                
n=int(input("Enter the number :"))
LEFT_TRUNCATABLE_PRIMES(n)
    
    