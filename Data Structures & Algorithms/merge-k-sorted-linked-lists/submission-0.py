# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for list in lists:
            curr = list
            while curr:
                arr.append(curr.val)
                curr = curr.next

        arr.sort()
        dummy = ListNode(-1)
        curr = dummy
        for num in arr:
            newNode = ListNode(num)
            curr.next = newNode
            curr = curr.next

        return dummy.next
