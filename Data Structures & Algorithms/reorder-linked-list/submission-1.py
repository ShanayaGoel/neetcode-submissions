# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return
        # calculate midpoint num
        counter = 0
        curr = head
        while curr is not None:
            counter += 1
            curr = curr.next
        midpoint = counter//2
        # counter var
        # create second head
        curr = head
        # traverse 2nd head till past midpoint
        for i in range(midpoint):
            curr = curr.next
        # begin attempt to reverse 2nd half of linked list
        # iterate through 2nd half
        prev = curr
        prev.next, curr = None, curr.next
        while curr is not None:
            
            next2 = curr.next
            curr.next = prev
            prev = curr
            curr = next2
        curr = prev
        # recreate list by merging/alternating and weaving
        curr1 = head

        while curr1 is not None:
            next1 = curr1.next
            curr1.next = curr
            if curr is not None:
                next2 = curr.next
                curr.next = next1
                curr = next2
            curr1 = next1
        return


