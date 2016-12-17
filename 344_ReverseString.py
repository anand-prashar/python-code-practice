'''
Write a function that takes a string as input and returns the string reversed.
'''
def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    l=list(s)
    
    rightIndex = -1
    for leftIndex in range(0,len(l)/2):
        temp = l[leftIndex]
        l[leftIndex] = l[rightIndex]
        l[rightIndex] = temp
        rightIndex-=1
    
    return ''.join(l)

print reverseString('hello')    
    