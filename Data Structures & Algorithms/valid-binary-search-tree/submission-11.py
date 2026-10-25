# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(node: Optional[TreeNode], left_bound: float, right_bound: float):
            if node is None:
                return True
            elif node.val <= left_bound or node.val >= right_bound:
                return False
            left_check = check(node.left, left_bound, node.val)
            right_check = check(node.right, node.val, right_bound)
            return left_check and right_check
        
        return check(root, float("-inf"), float("inf"))
                
            


