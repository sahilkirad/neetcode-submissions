# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # value -> index in inorder
        inorder_map = {}
        for i, val in enumerate(inorder):
            inorder_map[val] = i

        def build(preStart, preEnd, inStart, inEnd):

            # Base case
            if preStart > preEnd:
                return None

            # 1. Root is always the first element in preorder
            root = TreeNode(preorder[preStart])

            # 2. Find root in inorder
            rootIndex = inorder_map[root.val]

            # 3. Number of nodes in left subtree
            leftSize = rootIndex - inStart

            # 4. Build left subtree
            root.left = build(
                preStart + 1,
                preStart + leftSize,
                inStart,
                rootIndex - 1
            )

            # 5. Build right subtree
            root.right = build(
                preStart + leftSize + 1,
                preEnd,
                rootIndex + 1,
                inEnd
            )

            return root

        return build(
            0,
            len(preorder) - 1,
            0,
            len(inorder) - 1
        )