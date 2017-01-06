'''
Created on Dec 29, 2016

@author: anand
'''
def combination(inputList, combinationSize):
    
    if combinationSize > len(inputList) : return []
    if combinationSize == len(inputList): return [inputList]
    combinationList = []
    
    #logic
    for i in range(len(inputList)):
        
        combination = [inputList[i]]
        goDeep(inputList, i,combinationSize -1, combination)
        combinationList.append(combination)
    
    return combinationList    

def goDeep(inputList, doNotBuildIndex, combinationSize ,combination ):
    if combinationSize == 0: return
    for i in range(len(inputList)):
        if i != doNotBuildIndex:
            combination.append(inputList[i])
            goDeep(inputList, doNotBuildIndex,combinationSize-1,combination)   
    
    
            
            
print combination([1,2,3,4,5], 2)        