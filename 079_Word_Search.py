'''
Created on Dec 30, 2016

@author: anand
'''
class Solution(object):
    def exist(self, board, word):
        
        if len(board)==0: return False
        if len(word) > len(board)*len(board[0]): return False
 
        dictionary={}
        for rowIndex in range(len(board)):
            for colIndex in range(len(board[0])):
                if board[rowIndex][colIndex] not in dictionary:
                    dictionary.setdefault( board[rowIndex][colIndex], [(rowIndex,colIndex)] )
                else:
                    dictionary[ board[rowIndex][colIndex]].append( (rowIndex,colIndex) )
        
        prevList = None
        currList = None
        alreadyDoneIndex = {}
        for charIndex in range(len(word)):
            if word[charIndex] not in dictionary: return False
            if charIndex == 0:
                prevList = dictionary[ word[charIndex]] 
                continue
            else:
                currList = dictionary[ word[charIndex]]
            
            possiblePosforCurrItem = self.getAdjCellIndex(prevList, len(board), len(board[0]))
            common = []
            for position in currList:
                if (position in possiblePosforCurrItem) and (position not in alreadyDoneIndex):
                    common.append(position)
            if common == []: return False
        
            if len(prevList) == 1: 
                alreadyDoneIndex = prevList
            prevList = common    
        return True
    
    def getAdjCellIndex(self, currPositionList, maxRow, maxCol):
        adjList = {}
        for currPosition in currPositionList:
            if currPosition[0]+1<maxRow: adjList.setdefault( (currPosition[0]+1, currPosition[1]))                       
            if currPosition[0]-1>=0: adjList.setdefault( (currPosition[0]-1, currPosition[1]))  
            if currPosition[1]+1<maxCol: adjList.setdefault( (currPosition[0], currPosition[1]+1))                       
            if currPosition[1]-1>=0: adjList.setdefault( (currPosition[0], currPosition[1]-1)) 
        return adjList 

obj = Solution()
word = 'ABCESEEEF'
#===============================================================================
# board = [
#           ['A','B','C','E'],
#           ['S','F','C','S'],
#           ['A','D','E','E']
#         ]
#===============================================================================
#board = ["aaa","abb","abb","bbb","bbb","aaa","bbb","abb","aab","aba"]
board = ["ABCE","SFES","ADEE"]

print obj.exist(board, word)    