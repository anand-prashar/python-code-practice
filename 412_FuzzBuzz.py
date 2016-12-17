'''
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output 'Fizz' instead of the number and for the multiples of five output 'Buzz'. 
For numbers which are multiples of both three and five output 'FizzBuzz'.
'''
def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    
    retVal = []
    
    for i in range(1, n+1):
        if i%15==0:
            retVal.append('FizzBuzz')
        elif i%3==0:
            retVal.append('Fizz')
        elif i%5==0:
            retVal.append('Buzz')
        else: retVal.append(str(i))  
    
    return retVal

print fizzBuzz(15)          