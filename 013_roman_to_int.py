'''
Created on Dec 19, 2016

@author: anand
'''

def romanToInt(s):
    """
    :type num: int
    :rtype: str
    """
    mapp = { 
             ''  : 0, 
             'I' : 1,
             'IV': 4,
             'V' : 5,
             'IX': 9,
             'X' : 10,
             'XL': 40,
             'L' : 50,
             'XC': 90,
             'C' : 100,
             'CD': 400,
             'D' : 500,
             'CM': 900,
             'M' : 1000
            }
    
    num = 0
    while s != '':
            if len(s) > 1 and mapp[s[0]]<mapp[s[1]]:
                num+=mapp[s[1]] - mapp[s[0]]
                s = s[2:]
            else:
                num+= mapp[ s[0] ]
                s = s[1:]    
    return num

print romanToInt("XLIX")        