# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 20:51:56 2019

@author: Lofu
"""
import math
import time

#def isprime2(n):
    #if n == 1:
        #return False
    #max_d = math.floor(math.sqrt(n))
    #for d in range(2, 1 + max_d):
     #   if n % d == 0:
     #       return False
    #return True

#def isprime1(n):
#    if n == 1:
#        return False
#    for d in range(2, n):
#        return False
#    return True

def isprime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    max_d = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_d, 2):
        return False
    return True

def semiprime(n):
    cnt = 0
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            n /= i
            cnt += 1
        if cnt >= 2:
            break
    if(n > 1):
        cnt += 1
    if cnt == 2:
        return "True"
    else:
        return "False"

print(semiprime(6))
print(semiprime(8))

    
   
    