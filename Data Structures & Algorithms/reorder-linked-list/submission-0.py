# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast:
            prev_node = slow
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                fast = fast.next

        if prev_node: prev_node.next = None
        
        # slow is the starting where I want to start reversing
        prev = None
        current = slow

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        curr = head
        curr2 = prev

        while curr and curr2:
            temp = curr.next
            temp2 = curr2.next
            curr.next = curr2
            curr2.next = temp
            curr2 = temp2
            curr = temp

        return None

