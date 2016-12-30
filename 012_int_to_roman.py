'''
Created on Dec 19, 2016

@author: anand
'''

def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    dictionary = {
                 1:'I',
                 4:'IV',
                 5:'V',
                 9:'IX',
                 10:'X',
                 40:'XL',
                 50:'L',
                 90:'XC',
                 100:'C',
                 400:'CD',
                 500:'D',
                 900:'CM',
                 1000:'M'
                }            
    
    roman = ''
    for landmark in sorted( dictionary.keys(), reverse =True) :
        while num >= landmark:     
                roman += dictionary[landmark] 
                num   -= landmark   
                        
    return roman

print intToRoman(900)      