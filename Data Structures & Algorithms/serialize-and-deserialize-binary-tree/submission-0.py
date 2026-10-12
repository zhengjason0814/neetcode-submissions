# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        answer = []
        def serialdfs(root):
            if not root:
                answer.append("N")
                return None
            answer.append(str(root.val))
            serialdfs(root.left)
            serialdfs(root.right)
        
        serialdfs(root)
        return ",".join(answer)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        string = data.split(",")
        i = 0
        def deserial():
            nonlocal i
            if string[i] == "N":
                i += 1
                return None
            root = TreeNode(int(string[i]))
            i += 1
            root.left = deserial()
            root.right = deserial()
            
            return root
        return deserial()

            