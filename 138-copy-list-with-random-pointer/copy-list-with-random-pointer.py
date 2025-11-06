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
        memory = {None: None}

        curr = head
        # just make a copy of everything. dont worry about mapping
        while curr:
            memory[curr] = ListNode(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            memory[curr].next = memory[curr.next]
            memory[curr].random = memory[curr.random]
            curr = curr.next
        
        return memory[head]
        