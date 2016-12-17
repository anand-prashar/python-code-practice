'''
Given a non-empty string check if it can be constructed by taking a substring of it 
and appending multiple copies of the substring together. 
You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
'''
    
def repeatedSubstringPattern(userStr):
    """
    :type str: str
    :rtype: bool
    """
    if len(userStr) == 1: return False
    
    charCountDict = {}
    for c in userStr:
        if c not in charCountDict:
            charCountDict.setdefault(c,1)
        else:
            charCountDict[c]+=1
    
    print charCountDict
    
    minOccouringCount = None
    for v in charCountDict.values(): 
            if minOccouringCount !=None and minOccouringCount>v: minOccouringCount = v
            elif minOccouringCount == None: minOccouringCount = v
    print minOccouringCount
    
    assumedSampleLength = 0
    for k,v in charCountDict.iteritems():
        if v%minOccouringCount != 0: 
            return False
        else:
            charCountDict[k] = charCountDict[k] / minOccouringCount  
            assumedSampleLength+=charCountDict[k] 
    
    print charCountDict
    
    assumedSample = userStr[0: assumedSampleLength ]
    if assumedSample == userStr: return False
    for c in assumedSample:
        charCountDict[c]  -= 1
    
    print assumedSample
    print charCountDict
        
    for v in charCountDict.values():
        if v!=0: return False
    
    print assumedSample              
    return True                  
    

print repeatedSubstringPattern('')    