class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # we must make sure there are no cycles

        # create an adj list mapping each course to courses it is a prereq to one directionally
        adj = {i:[] for i in range(numCourses)}
        for pre in prerequisites:
            adj[pre[0]].append(pre[1])

        # set of visited nodes to track master and to be changed
        master = set()
        curr_visited = set()
        
        def dfs(a, visited, node):
            # if in curr visited  False is returned
            if node in visited:
                return False
            # add into curr visited
            visited.add(node)
            # run dfs on neighbors
            for n in a[node]:
                if n not in master:
                    result = dfs(a, visited, n)
                    if not result:
                        return False
            master.add(node)
            # if any return false, return false
            # otherwise remove from current visited and return true
            visited.remove(node)
            return True
                
        #iterate through each node in adj, if it is not in visited in master visited

            # in each iteration, reassign the current visited to new empty set
        for pre in adj:
            if pre not in master:
                curr_visited = set()
                if not dfs(adj, curr_visited, pre):
                    return False
        return True
        
        
