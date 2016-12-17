'''
Given a string s, find the longest palindromic substring in s.

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
'''

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    
    lowLimit = 0
    highLimit = len(s)
    palindrome = ''
   
    for index in range(0,highLimit):
        
        dist = 1
        if (index!=highLimit-1) and (s[index] == s[index+1]):
            searchEvenString = True
            tempPalindrome = ''
        else:
            searchEvenString = False 
            tempPalindrome = s[index]
        
            
        if searchEvenString:
            while ( index-dist+1>=lowLimit and index+dist <highLimit) and  (s[index-dist+1] == s[index+dist]):
                tempPalindrome = s[index-dist+1] + tempPalindrome + s[index+dist]
                dist+=1
        else:           
            while ( index-dist>=lowLimit and index+dist <highLimit) and  (s[index-dist] == s[index+dist]):
                tempPalindrome = s[index-dist] + tempPalindrome + s[index+dist]
                dist+=1
            
        if len(tempPalindrome) > len(palindrome):
            palindrome = tempPalindrome    
    
    return palindrome      
    

print longestPalindrome('ccc')      