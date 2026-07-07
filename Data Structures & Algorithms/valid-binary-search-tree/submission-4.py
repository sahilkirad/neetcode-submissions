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
        st=[]
        current=root
        prev=None
        while current or st:

            while current:
                st.append(current)
                current=current.left
            current=st.pop()
            if prev is not None and current.val<=prev.val:
                return False
            prev=current
            current=current.right
        return True