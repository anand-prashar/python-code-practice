'''
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") => false
isMatch("aa","aa") => true
isMatch("aaa","aa") => false
isMatch("aa", "a*") => true
isMatch("aa", ".*") => true
isMatch("ab", ".*") => true
isMatch("aab", "c*a*b") => true
'''

def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    
    if not( '*' in p or '.' in p):
        return s == p
    
    tempPattern = ''
    pIndex = 0
    lastChar =''
    while pIndex< len(p):
        if p[pIndex] == '*' and pIndex<len(p)-1 and (p[pIndex-1]==p[pIndex+1]):
            tempPattern+=p[pIndex]
            
            lastChar = p[pIndex-1]
            while pIndex<len(p) and (lastChar == p[pIndex] or p[pIndex]=='*'): 
                pIndex+=1
            continue
        tempPattern+=p[pIndex]
        pIndex+=1
    
    print 'old Pattern=',p,'\nnew Pattern=',tempPattern
    p = tempPattern
            
    
    sPointer = 0
    for i in range(len(p)):
        # if sPointer>=len(s): break
        
        if p[i] == '*':
            if p[i-1] != '.':
                while sPointer<len(s) and s[sPointer] == p[i-1]:
                    sPointer+=1
                continue    
            else:
                if (i+1)<len(p):  
                    while sPointer<len(s) and s[sPointer] != p[i+1]:
                        sPointer+=1
                else:
                    sPointer = len(s)
                    break  
        elif p[i] == '.':
            if i+1 < len(p) and p[i+1] == '*': continue
            sPointer+=1
            continue     
        else:  # any other char
            if i+1 < len(p) and p[i+1] == '*': continue
            if sPointer<len(s) and s[sPointer]!= p[i]: break
            sPointer+=1
            continue        
                
    
    print 'sPointer=', sPointer, 'S_len', len(s)
    print 'i+1=',i+1, 'P_len', len(p)
    
    return sPointer == len(s) and i+1 == len(p)  


#===========================================================================
    
print isMatch('aaab', 'ab*a*c*ab')    