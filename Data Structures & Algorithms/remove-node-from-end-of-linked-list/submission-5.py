# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        n_behind = head
        node = head
        if head.next is None:
            return None
        for i in range(n):
            node = node.next
        if node is None:
            head = head.next
            return head
        
        while node.next is not None:
            node, n_behind = node.next, n_behind.next
        n_behind.next = n_behind.next.next
        return head