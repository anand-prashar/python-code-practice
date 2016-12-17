'''
Created on Dec 15, 2016

@author: anand
'''

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    
    if x<0: return False
    otherNumber = 0
    bkp = x
    
    pwr = -1
    while bkp>0:
        bkp/=10
        pwr+=1
        
    bkp = x
    while bkp > 0:
        otherNumber += (bkp%10)*pow(10,pwr)   
        bkp/=10
        pwr-=1
    
    return x == otherNumber    

print isPalindrome(00)