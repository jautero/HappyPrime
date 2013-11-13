#!/usr/bin/env python
# 
#  HappyPrime.py
#  HappyPrime
#
#  Create happy primes. Happy primes are cool.  (I know, that's 11th doctor, not 10th)
#  Created by Juha Autero on 2013-11-13.
#  Copyright 2013 Juha Autero. All rights reserved.
# 

def sumSquareDigits(number):
    sum=0
    while number > 0:
        digit=number % 10
        sum+=digit*digit
        number/=10
    return sum

def getNextHappyPrime(happy_prime):
    number=nextPrime(happy_prime)
    while not isHappy(number):
        number=nextPrime(number)
    return number
    
def isHappy(number):
    if number == 1:
        return True
    old=number
    number=sumSquareDigits(number)
    updateold=False
    while number != 1:
        if old==number:
            return False
        if updateold:
            old=sumSquareDigits(old)
        updateold=not updateold
        number=sumSquareDigits(number)
    return True

def isPrime(number):
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    divisor=3
    while divisor*divisor<=number:
        if number % divisor == 0:
            return False
        divisor+=2
    return True

def nextPrime(number):
    number+=1
    while not isPrime(number):
        number+=1
    return number

if __name__ == '__main__':
    import sys
    print getNextHappyPrime(int(sys.argv[1]))
