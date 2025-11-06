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
        if not head:
            return None
        #interleave original and copy
        l1 = head
        while l1:
            l2 = Node(l1.val)
            l2.next = l1.next
            l1.next = l2

            l1 = l2.next
        
        # connect the randoms of copy
        l1 = head
        while l1:
            if l1.random:
                l1.next.random = l1.random.next
            l1 = l1.next.next
        
        # disconnect original and duplicate
        l1 = head
        l2 = l1.next
        dummy = l2
        while l1:
            l1.next = l2.next
            
            if l2.next:
                l2.next = l2.next.next

            l1 = l1.next
            l2 = l2.next
        
        return dummy