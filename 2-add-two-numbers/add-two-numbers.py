# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        node = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total_sum = v1 + v2 + carry

            digit = total_sum % 10
            carry = total_sum // 10

            node.next = ListNode(digit)
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            node = node.next
        
        return dummy.next