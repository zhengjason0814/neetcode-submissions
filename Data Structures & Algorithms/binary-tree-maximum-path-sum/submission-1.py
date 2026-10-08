# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answer = root.val

        def dfs(root):
            nonlocal answer

            if not root:
                return 0

            leftMax, rightMax = dfs(root.left), dfs(root.right)
            leftMax, rightMax = max(leftMax, 0), max(rightMax, 0)

            answer = max(answer, root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return answer