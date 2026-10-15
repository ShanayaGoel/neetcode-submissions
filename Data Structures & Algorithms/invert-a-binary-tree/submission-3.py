# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        if root.left == None and root.right == None:
            return root
        elif root.right == None :
            left_tree = self.invertTree(root.left)
            right_tree = root.right
            root.left, root.right = right_tree, left_tree
            return root
        elif root.left == None :
            left_tree = root.left
            right_tree = self.invertTree(root.right)
            root.left, root.right = right_tree, left_tree
            return root
        left_tree = self.invertTree(root.left)
        right_tree = self.invertTree(root.right)
        root.right = left_tree
        root.left = right_tree
        return root
        
        