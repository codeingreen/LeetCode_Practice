# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        sentinel = ListNode(0)
        sentinel.next = head
        
        # sentinel has the path of prev
        # we want to return sentinel.next which stores head
        prev, cur = sentinel, head
        
        while cur:
            
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            
            cur = cur.next
        
        return sentinel.next
