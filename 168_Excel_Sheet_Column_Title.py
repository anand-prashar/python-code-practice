'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''

charDict = []
outputString = ''
i=65
while i<=90:
    charDict.append(chr(i))
    i+=1

#print charDict    
try:
    num = long(raw_input('Enter number:'))
    charLength = len(charDict)

    while num > 0:
        
        mod = num%charLength
        outputString = charDict[ mod-1 ] + outputString  # notice the order of append
        if mod ==0:
            num=num/charLength -1  ######### if mod = 0, means that char was Z, then substract 1 as well
        else:
            num/=charLength
                
except :
    pass
        

print outputString