"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #begin from root
        # keep a check of existing root map to new root
        # 
        old_to_new = {}
        def go(node, match):
            if node is None:
                return None
            elif node in match:
                return match[node]
            new_node = Node(node.val)
            match[node] = new_node
            for n in node.neighbors:
                new_node.neighbors.append(go(n, match))
            return new_node
        
        return go(node, old_to_new) 