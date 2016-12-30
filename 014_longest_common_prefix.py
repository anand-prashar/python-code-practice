'''
Write a function to find the longest common prefix string amongst an array of strings.
'''

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    
    minString = strs[0]
    for string in strs:
        if len(string)<len(minString):
            minString = string
    
    lookupString = ''
    L = 0
    R = len(minString)
    strs.remove(minString)
    
    while True:
        mid = (L+R)/2
        lookupString = minString[L:mid]
        noOfMatchedStrings = 0
        for string in strs:
            if lookupString in string:
                noOfMatchedStrings+=1
        if noOfMatchedStrings == len(strs):
                    
    print minLength
    
longestCommonPrefix(['ana','xy'])    