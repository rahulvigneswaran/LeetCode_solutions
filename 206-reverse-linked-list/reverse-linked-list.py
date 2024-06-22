# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_head = None
        while head:
            temp_next = head.next
            head.next = prev_head
            prev_head = head 
            head = temp_next
        return prev_head