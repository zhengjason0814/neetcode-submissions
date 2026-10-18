"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyDict = {None : None}
        current = head

        while current:
            copyDict[current] = Node(current.val)
            current = current.next
        
        current = head
        while current:
            copyDict[current].next = copyDict[current.next]
            copyDict[current].random = copyDict[current.random]
            current = current.next

        return copyDict[head]

        
