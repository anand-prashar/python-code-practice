
'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
'''

class Solution(object):
    def isPalindrome(self, s):  
        
        leftIndex,rightIndex = 0,len(s)-1
        while leftIndex < rightIndex:
            while leftIndex < rightIndex and  not s[leftIndex].isalnum()  :  leftIndex +=1
            while leftIndex < rightIndex and  not s[rightIndex].isalnum() : rightIndex -=1
            
            if s[leftIndex].lower() != s[rightIndex].lower(): return False
            leftIndex +=1
            rightIndex-=1
        return True    

          
    #===========================================================================
    # def isPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """
    #     
    #     dict = {}
    #     for i in range(ord('A'),ord('Z')+1):
    #         dict.setdefault(chr(i),True)
    #         dict.setdefault(chr(i+32), True)
    #         dict.setdefault(str(i%10),True )
    #     
    #     newS = []
    #     for c in s:
    #         if c in dict:
    #             newS.append( c.lower())
    #     
    #     print 'NEW len= ',len(newS)
    #     length = len(newS)
    #     if length in [0,1]: return True
    #     
    #     center = length/2
    #     if length%2!=0:
    #         #print 'Odd'
    #         for i in range(0,center+1):
    #             if newS[center+i] != newS[center-i]: return False
    #     else:
    #         for i in range(0,center):
    #             if newS[center+i] != newS[center-i-1]: return False
    #     
    #     return True
    #===========================================================================

obj = Solution()
f = open('125.txt')
l = ''
for line in f:
    l+=line
print obj.isPalindrome(l)                