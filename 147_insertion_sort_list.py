'''
Sort a linked list using insertion sort
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if (head is None) or (head.next is None): return head
        
        returnHead = head
        head = head.next
        returnHead.next = None
        
        while head is not None:
            tempIterator = returnHead
            prev = None
            while (tempIterator!=None and (tempIterator.val < head.val) ):
                prev= tempIterator
                tempIterator = tempIterator.next
            
            temp = head
            head = head.next    
            if prev == None:
                temp.next = tempIterator
                returnHead = temp
            else:
                temp.next = prev.next
                prev.next = temp
        
        return returnHead        
                        

###################################### 

root = ListNode(4)
root.next = ListNode(5)
root.next.next = ListNode(3)
root.next.next.next = ListNode(2)


obj = Solution()
root = obj.insertionSortList(root)

while root is not None:
    print root.val, ' ->'
    root = root.next