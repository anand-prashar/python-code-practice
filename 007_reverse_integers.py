'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
'''
from __builtin__ import True

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    retVal = 0
    power = -1
    reverse = False
    if x<0: reverse = True;x = x*-1
    
    cpy = x
    while cpy!=0:
        cpy= cpy/10
        power+=1
    
    while x != 0:
        retVal+= x%10 * pow(10,power)
        power-=1
        x/=10
    if reverse: retVal*=-1
    return retVal


print reverse(1534236469)    