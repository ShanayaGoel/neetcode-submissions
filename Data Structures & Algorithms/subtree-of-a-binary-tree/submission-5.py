# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        
        def dfs(curr_root: Optional[TreeNode], curr_sub: Optional[TreeNode]) -> bool:
            l = True
            r = True
            #check this root
            if curr_root.val != curr_sub.val:
                return False
            if curr_sub.left is not None:
                if curr_root.left is None:
                    return False
                else:
                    l = dfs(curr_root.left, curr_sub.left )
            elif curr_root.left is not None:
                return False
            
            if curr_sub.right is not None:
                if curr_root.right is None:
                    return False
                else:
                    r = dfs(curr_root.right, curr_sub.right )
            elif curr_root.right is not None:
                return False
            
            return l and r

        # if root is equal, run 
        def find_pos(rt, sb) -> bool:
            if rt is None:
                return False
            elif rt.val == sb.val:
                if dfs(rt, sb):
                    return True
            return find_pos(rt.left, sb) or find_pos(rt.right, sb)
        return find_pos(root, subRoot)