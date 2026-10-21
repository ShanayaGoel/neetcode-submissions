# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        new_list = None
        last_node = None
        l1 = list1
        l2 = list2
        if l1.val < l2.val:
            new_list = list1
            last_node = list1
            l1 = l1.next
        else:
            new_list = list2
            last_node = list2
            l2 = l2.next
        
        

        while l1 is not None or l2 is not None:
            if l1 is None:
                last_node.next = l2
                l2 = None
            elif l2 is None:
                last_node.next = l1
                l1 = None
            else:

                if l1.val < l2.val:
                    last_node.next = l1
                    last_node = l1
                    l1 = l1.next
                else:
                    last_node.next = l2
                    last_node = l2
                    l2 = l2.next
        return new_list