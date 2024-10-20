# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not(lists) or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i+1) < len(lists) else None
                mergedLists.append(merge2List(l1, l2))
            lists = mergedLists
        
        return lists[0]

def merge2List(l1, l2):
    node = ListNode()
    res = node

    while l1 and l2:
        if l1.val < l2.val:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next
        node = node.next
    if l1:
        node.next = l1
    if l2:
        node.next = l2
    
    return res.next

# we should do the same merging of 2 lists but do it in a merge sort fashion