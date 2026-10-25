# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        multiplier = 1
        numOne = 0
        current = l1
        while current:
            numOne += current.val * multiplier
            multiplier *= 10
            current = current.next
        
        multiplier = 1
        numTwo = 0
        current = l2
        while current:
            numOne += current.val * multiplier
            multiplier *= 10
            current = current.next
        
        sum = numOne + numTwo
        answer = ListNode(sum % 10)
        sum = sum // 10
        current = answer
        while sum > 0:
            current.next = ListNode(sum % 10)
            sum = sum // 10
            current = current.next
        
        return answer