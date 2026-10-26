class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # create an adjacency list mapping each node to its neighbors
        nodes = {node:[] for node in range(n)}
        for edge in edges:
            nodes[edge[0]].append(edge[1])
            nodes[edge[1]].append(edge[0])
        # create empty visited set
        visited = set()
        # dfs recursive function (params = root, node, visited)
        def dfs(prev, node, visit):

            # if in visited, return false
            if node in visit:
                return False
            # iterate through each of its neighbors other than where it came from with dfs
            visit.add(node)
            for neighbor in nodes[node]:
                if neighbor != prev:
                    if not dfs(node, neighbor, visit):
                        return False
            # if any are false, return false
            # add to visited
            
            # return true if we have reached this point
            return True
        # call dfs function on node 0 and if i
        return dfs(-1, 0, visited) and len(visited) == n

        # return dfs and visited has a length of n
               