# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # handle
        dummy = ListNode(0)
        dummy.next = head

        # finding kth node from last
        start = dummy
        end = dummy

        for i in range(n+1):
            if end:
                end = end.next
        
        while end:
            start = start.next
            end = end.next
        
        # removing the kth node
        start.next = start.next.next
        
        return dummy.next

# Have two pointers. push the second pointer to n+1 position first. Then move both start and end till end reaches node. This would make the start exactly 1 position before the node we want to remove. Now remove it. Create a dummy node and point to the head to handle base cases.

# Time complexity >> O(n)
# Space complexity >> O(1)