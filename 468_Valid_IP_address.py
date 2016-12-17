'''
Created on Dec 16, 2016

@author: anand

In this problem, your job to write a function to check whether a input string is a valid IPv4 address or IPv6 address or neither
'''

def validIPAddress(IP):
    """
    :type IP: str
    :rtype: str
    """
    
    ip4 = '.' in IP
    ip6 = ':' in IP
    
    if (ip4 and ip6) or not(ip4 or ip6):
        return 'Neither'
    
    if ip4:
        numList = IP.split('.')
        if len(numList) != 4: return 'Neither'
        
        for numC in numList:
            try:
                if len(numC)> 1 and (numC[0] in ['0','-','+'] ): return 'Neither'
                
                if not( 0 <= int(numC)<= 255):
                    return 'Neither'
                
            except ValueError:
                return 'Neither' 
        
        return 'IPv4'
           
    if ip6:
        hexLookupDict = {}
        for i in range(10):
            hexLookupDict.setdefault(str(i))
        for i in range(65,71): #A-E
            hexLookupDict.setdefault(chr(i))     #Caps
            hexLookupDict.setdefault(chr(i+32))  #small letters
                
        hexList = IP.split(':')
        if len(hexList) != 8: return 'Neither'
        
        
        for hexC in hexList:
            if not( 1<=len(hexC)<=4): 
                return 'Neither'
            for c in hexC:
                if not (c in hexLookupDict):
                    return 'Neither'
        return 'IPV6'        
         

print validIPAddress('15.16.-0.1')        