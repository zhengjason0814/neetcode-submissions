# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def findSize(root):
            if not root:
                return
            arr.append(root.val)
            findSize(root.left)
            findSize(root.right)
        findSize(root)
        target = sorted(arr)[k - 1]
    
        while root.val != target:
            if root.val > target:
                root = root.left
            else:
                root = root.right
        
        return root.val