# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(curr_root: TreeNode) -> List[int]:
            list_of_sub = []

            # left branch
            if curr_root.left is not None:
                list_of_sub += dfs(curr_root.left)
            # root
            list_of_sub.append(curr_root.val)
            #right branch
            if curr_root.right is not None:
                list_of_sub += dfs(curr_root.right)
            return list_of_sub
        return dfs(root)[k-1]

        
        