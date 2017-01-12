'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as 

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    __is_Balanced = True
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root != None: self.iterate(root)
        return self.__is_Balanced
    
    def iterate(self, node):
        if node.left==None and node.right == None: 
            return 0
        
        if node.left!= None: leftHeight  = self.iterate(node.left)
        else: leftHeight = -1
        if node.right!= None: rightHeight = self.iterate(node.right)
        else: rightHeight = -1
        
        if abs(leftHeight-rightHeight)>1: self.__is_Balanced = self.__is_Balanced & False
        return max([leftHeight, rightHeight])+1


root = TreeNode(1) 
root.left = TreeNode(2)
root.left.left = TreeNode(4)
#root.left.left.left = TreeNode(5)
root.right = TreeNode(3)

obj = Solution()
print obj.isBalanced(root)