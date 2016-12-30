'''
Created on Dec 29, 2016

@author: anand
'''
def combination(inputList, doNotAddIndex, remainingSize, combList):
    if remainingSize == 0: return
    
    for i in range(len(inputList)):
        if i not in doNotAddIndex:
            combList.append(inputList[i])
            doNotAddIndex.append(i)
            combination(inputList, doNotAddIndex, remainingSize-1, combList)
        
    return combList 
            
            
print combination([1,2,3], [], 2, [])        