class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #create adj list mapping all nodes to all neighbors\
        adj = {i:[] for i in range(n)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        #counter
        counter = 0
        # visited var set with all the visited nodes
        visited = set()
        # dfs on each node in adj if it is not in visited
        def dfs(adjacent, visited, node):
            # if in visited return
            if node in visited:
                return
            # if not add to visited
            else:
                visited.add(node)
                for n in adj[node]:
                    dfs(adjacent, visited, n)
        
        # upon running dfs on each, add 1 to counter each time
        for i in adj:
            if i not in visited:
                dfs(adj, visited, i)
                counter += 1

        #return counter
        return counter