# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # have a set of visited nodes
        # init visisted as empty
        visited = set()
        node = head
        if head is None:
            return False

        # iterate until either we reach a visited(False) or None (True)
        while node is not None:
            visited.add(node)
            if node.next in visited:
                return True
            node = node.next
        return False