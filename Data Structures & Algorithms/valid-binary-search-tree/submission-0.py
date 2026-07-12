# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def checky(root):
    #     while root:
    #         if root.left>root.val or root.right<root.val:
    #             return False
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if root.left.val>root.val or root.right.val<root.val:
            return False
        else:
            return True
        left=isValidBST(root.left)
        right=isValidBST(root.right)
        return left and right