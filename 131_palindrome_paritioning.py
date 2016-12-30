'''
Created on Dec 28, 2016

@author: anand
'''

class Solution(object):
    
    def manacher(self, string):
    
        maxSubStr = ''
        for i in range(len(string)):
            #odd
            subStrOdd = string[i]
            subStrEven = ''
            itr = 1
            evenContinue = True
            oddContinue = True
            
            while evenContinue or oddContinue:
                if oddContinue and ( (i-itr)>=0 and (i+itr)<len(string) ) and (string[i-itr] == string[i+itr]):
                    subStrOdd =string[i-itr] + subStrOdd + string[i+itr]
                else:
                    oddContinue = False
                
                if evenContinue and ( (i-itr+1)>=0 and (i+itr)<len(string) ) and (string[i-itr+1] == string[i+itr]):
                    subStrEven = string[i-itr+1] + subStrEven + string[i+itr]
                else:
                    evenContinue = False    
                itr+=1    
                    
            #print string[i] ,' : ',subStrOdd, ',', subStrEven
            if len(maxSubStr) < len(subStrEven): maxSubStr = subStrEven
            if len(maxSubStr) < len(subStrOdd):  maxSubStr = subStrOdd
            
        return maxSubStr 
        
    def recursiveSoln(self, s, palList): 
        if s == '': return
        maxPal = self.manacher(s)
        
        clipIndex1 = s.index(maxPal)
        clipIndex2 = clipIndex1 + len(maxPal)

        if clipIndex1>=0: self.recursiveSoln( s[0: clipIndex1], palList)
        palList.append(maxPal)
        if clipIndex2<len(s):self.recursiveSoln( s[clipIndex2:len(s)], palList)
        
        
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        palList = []
        superList = []
        self.recursiveSoln( s[0:len(s)], palList)
        
        #print palList
        superList.append(palList)
        return superList
    
#######################################################################

obj = Solution()
obj.partition('abbaANANAhello')