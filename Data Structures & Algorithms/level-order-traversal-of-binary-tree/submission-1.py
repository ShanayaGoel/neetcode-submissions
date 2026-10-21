# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs traversal

        if root is None:
            return []
        list_tbr = [[root.val]]
        current_level = [root]
        while current_level != []:
            next_level = []
            next_level_values = []
            for i in current_level:
                if i.left != None:
                    next_level.append(i.left)
                    next_level_values.append(i.left.val)
                if i.right != None:
                    next_level.append(i.right)
                    next_level_values.append(i.right.val)
            current_level = next_level
            if next_level_values != []:
                list_tbr.append(next_level_values)
        return list_tbr