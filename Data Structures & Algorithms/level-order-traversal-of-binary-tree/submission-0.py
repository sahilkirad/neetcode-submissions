# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque()
        a=[]
       
        if root:
            queue.append(root)
        while queue:
            level=[]
            for _ in range(len(queue)):
                n1=queue.popleft()
                level.append(n1.val)
                if n1.left:
                    queue.append(n1.left)
                if n1.right:
                    queue.append(n1.right)
            a.append(level)
            
        

        return a