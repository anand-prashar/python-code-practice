'''
implement ATOI(121) // ATOI('QWQW12')
'''
import re

def myAtoi(myStr):
    """
    :type myStr: myStr
    :rtype: int
    """
    myStr = myStr.replace(' ','')
    if len(myStr) == 0: return 0
    
    charDict = {}
    for i in range(10):
        charDict.setdefault(str(i),i)
    
    if myStr[0] == '-':
        negativeNo = True
        myStr = myStr[1:]
    else:
        if myStr[0] == '+': myStr = myStr[1:]    
        negativeNo = False
    
    retVal = 0
    power = 0
    for i in range(1,len(myStr)+1):
        if myStr[-i] not in charDict: return 0
        retVal+=charDict[myStr[-i]]*pow(10, power)
        power+=1
    
    if negativeNo: 
        return retVal*-1
    return retVal     
    
num = myAtoi('+1')
#print 'Type = ', type(num)
print ', Value= ',num    