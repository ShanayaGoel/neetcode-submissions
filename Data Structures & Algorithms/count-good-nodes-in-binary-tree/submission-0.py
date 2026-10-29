# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # root is obviously good
        count = 0
        # run dfs to find number
        # dfs should have the max up till that point as a parameter alongside the current node
        def dfs(node: TreeNode, max_prev: int) ->int:
            max = max_prev
            # internal counter
            counter = 0
            # check if good, if good counter += 1
            if node.val >= max:
                counter += 1
                max = node.val
            # add in dfs of left if possible
            if node.left is not None:
                counter += dfs(node.left, max)
            # add in dfs of right if possible
            if node.right is not None:
                counter += dfs(node.right, max)
            return counter
        count = dfs(root, -239939393)
        return count