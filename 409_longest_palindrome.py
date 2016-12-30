'''
len of longest palindrome
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxSubStr = ''
        for i in range(len(s)):
            #odd
            subStrOdd = s[i]
            subStrEven = ''
            itr = 1
            evenContinue = True
            oddContinue = True
            
            while evenContinue or oddContinue:
                if oddContinue and ( (i-itr)>=0 and (i+itr)<len(s) ) and (s[i-itr] == s[i+itr]):
                    subStrOdd =s[i-itr] + subStrOdd + s[i+itr]
                else:
                    oddContinue = False
                
                if evenContinue and ( (i-itr+1)>=0 and (i+itr)<len(s) ) and (s[i-itr+1] == s[i+itr]):
                    subStrEven = s[i-itr+1] + subStrEven + s[i+itr]
                else:
                    evenContinue = False    
                itr+=1    
                    
            #even
            #print s[i] ,' : ',subStrOdd, ',', subStrEven
            if len(maxSubStr) < len(subStrEven): maxSubStr = subStrEven
            if len(maxSubStr) < len(subStrOdd):  maxSubStr = subStrOdd
        
        return len(maxSubStr)   
        
        #print
sol = Solution()
print sol.longestPalindrome('abccccdd')   