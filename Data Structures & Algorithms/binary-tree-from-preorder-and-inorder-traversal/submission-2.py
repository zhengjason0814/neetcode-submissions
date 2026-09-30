# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexHash = {}
        preOrderIndex = 0
        for i in range(len(inorder)):
            indexHash[inorder[i]] = i

        def dfs(l, r):
            nonlocal preOrderIndex
            if l > r:
                return None
            root = TreeNode(preorder[preOrderIndex])
            preOrderIndex += 1
            mid = indexHash[root.val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            
            return root
        
        return dfs(0, len(inorder) - 1)