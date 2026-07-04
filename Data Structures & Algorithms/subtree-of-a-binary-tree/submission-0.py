# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = rightw

class Solution:   
    def sameTree(self,root,subRoot):
        if root is None and subRoot is None:
            return True
        
        if root is None or subRoot is None:
            return False
        
        if root.val!=subRoot.val:
            return False
     
        left=self.sameTree(root.left,subRoot.left)
        right=self.sameTree(root.right,subRoot.right)

        return left and right
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if self.sameTree(root,subRoot):
            return True
        
       
        left=self.isSubtree(root.left,subRoot)
        
        right=self.isSubtree(root.right,subRoot)
        return left or right