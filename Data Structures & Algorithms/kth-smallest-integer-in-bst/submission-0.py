# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st=[]
        current=root
        prev=None
        
        while current or st:
            while current:
                st.append(current)
                current=current.left
            current=st.pop()
            k=k-1
            if k==0:
                return current.val
            prev=current
            current=current.right
        
        