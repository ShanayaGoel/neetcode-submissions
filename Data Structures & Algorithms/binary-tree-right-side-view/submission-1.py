# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        listtbr = []
        if root is None:
            return []
        curr_level = [root]
        next_level = []
        while len(curr_level) > 0:
            for node in curr_level:
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            listtbr.append(curr_level[len(curr_level)- 1].val)
            curr_level = next_level
            next_level = []

        return listtbr
