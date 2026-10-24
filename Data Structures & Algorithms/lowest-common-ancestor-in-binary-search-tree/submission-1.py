# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestor = root
        curr_root = root
        # keep going through the bst in the direction of p ad q, until you reach one or have to diverge
        #while left or right exists
        while curr_root.left is not None or curr_root.right is not None:
            # if opposite directions or equal
            if p.val >= curr_root.val and q.val <= curr_root.val:
                return curr_root
            elif p.val <= curr_root.val and q.val >= curr_root.val:
                return curr_root
            # else continue to traverse by going left if less or right if more
            else:
                if p.val < curr_root.val:
                    curr_root = curr_root.left
                elif p.val > curr_root.val:
                    curr_root = curr_root.right
        # if divergence has not been found, return originak


        #at this point we get the lowest common ancestor
