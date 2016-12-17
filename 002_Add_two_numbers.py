'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    
        root = None
        prevNode = None
        
        while l1 != None and l2 != None:
            currNode = ListNode(l1.val + l2.val)
            if root == None: root = currNode
            
            if prevNode != None: 
                prevNode.next = currNode
                if prevNode.val >= 10:
                    prevNode.val %= 10
                    currNode.val = currNode.val + 1
                    
            prevNode = currNode
            l1 = l1.next
            l2 = l2.next
        
        if l1 != None: largerList = l1
        else: largerList = l2   

        while largerList != None:
            if prevNode.val >= 10:
                prevNode.val %= 10
                prevNode.next = ListNode(largerList.val + 1)
            else:
                prevNode.next = ListNode(largerList.val)
            prevNode = prevNode.next
            largerList = largerList.next        
            
        if prevNode.val >= 10:
            prevNode.val %= 10
            prevNode.next = ListNode(1)
                
        return root

def addTwoNumbersRev(l1, l2):
    
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    
        listNo1 = []
        listNo2 = []
        
        while l1 != None:
            listNo1.append(l1.val)
            l1 = l1.next
        while l2 != None:
            listNo2.append(l2.val)
            l2 = l2.next    
        
        prevNode = None
        largerList = None
        maxCommonIndex = len(listNo1) - len(listNo2) 
        if maxCommonIndex >= 0:
            largerList = listNo1
        else:
            largerList = listNo2
        maxCommonIndex = abs(maxCommonIndex) - len(largerList)
                
        lastIndex = -1
        while lastIndex >= maxCommonIndex:
            numResult = listNo1[lastIndex] + listNo2[lastIndex]
            currNode = ListNode(numResult)
            currNode.next = prevNode
            
            if prevNode != None and prevNode.val >= 10:
                prevNode.val %= 10
                currNode.val += 1
                
            prevNode = currNode
            lastIndex -= 1
  
        currNode = ListNode(0)
        if prevNode != None and prevNode.val >= 10:
            prevNode.val %= 10
            currNode = currNode.val + 1
            currNode.next = prevNode
        
        while(maxCommonIndex != -len(largerList)):
                
                currNode.val += largerList[maxCommonIndex] 
                currNode.next = prevNode
                
                prevNode = currNode
                
        return prevNode
    
        

root1 = ListNode(2)
root1.next = ListNode(4)  
root1.next.next = ListNode(3)
# root1.next.next.next = ListNode(9)
# root1.next.next.next.next = ListNode(9)

root2 = ListNode(5)
root2.next = ListNode(6)  
root2.next.next = ListNode(4)              
                
valRes = addTwoNumbers(root1, root2)
while valRes != None:
    print valRes.val    
    valRes = valRes.next       
