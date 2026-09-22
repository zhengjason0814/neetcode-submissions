# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        answer = -1
        def inorder(root):
            nonlocal counter, answer
            if not root or answer != -1:
                return
            inorder(root.left)
            counter += 1
            if counter == k:
                answer = root.val
                return
            inorder(root.right)
        inorder(root)

        return answer