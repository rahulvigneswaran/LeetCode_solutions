# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        headFast = head
        while head.next != None and headFast.next != None:
            head = head.next
            headFast = headFast.next
            if headFast.next == None:
                break
            headFast = headFast.next

            if head == headFast:
                return True
        return False