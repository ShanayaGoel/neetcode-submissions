# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # perhaps create var to store new linked list
        if head is None:
            return None
        if head.next is None:
            return head
        # 
        prev = head
        node = head.next
        head.next = None
        while node.next is not None:
            next_node = node.next
            node.next = prev
            prev, node = node, next_node
        node.next = prev
        return node