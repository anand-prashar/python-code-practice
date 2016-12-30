'''
Created on Dec 28, 2016

@author: anand
Considering each character as a pivot, 
expand on both sides to find the length of both even and odd length palindromes centered at the pivot character 
under consideration and store the length in the 2 arrays (odd & even).
Time complexity for this step is O(n^2)
'''

def manacher(string):
    
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
                
        #even
        print string[i] ,' : ',subStrOdd, ',', subStrEven
        if len(maxSubStr) < len(subStrEven): maxSubStr = subStrEven
        if len(maxSubStr) < len(subStrOdd):  maxSubStr = subStrOdd
    
    print '\nMAX SUBSTRING = ', maxSubStr    
        
        #print

manacher('forgeeksskeegfor')        