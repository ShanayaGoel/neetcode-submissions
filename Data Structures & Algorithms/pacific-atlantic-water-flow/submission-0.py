class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #we want to create a list of all cells flowing to pacific
        pacific = set()
        atlantic = set()
        if len( heights) == 0 or len(heights[0]) == 0:
            return []
        def dfs(tracker, node):
            if tuple(node) in tracker:
                return
            tracker.add(tuple(node))
            if node[0] < len(heights) - 1:
                if heights[node[0]][node[1]] <= heights[node[0] + 1][node[1]]:
                    dfs(tracker, [node[0] + 1, node[1]])
            if node[0] > 0:
                if heights[node[0]][node[1]] <= heights[node[0] - 1][node[1]]:
                    dfs(tracker, [node[0] - 1, node[1]])
            if node[1] > 0:
                if heights[node[0]][node[1]] <= heights[node[0]][node[1]-1]:
                    dfs(tracker, [node[0], node[1]-1])
            if node[1] < len(heights[0]) - 1:
                if heights[node[0]][node[1]] <= heights[node[0]][node[1]+1]:
                    dfs(tracker, [node[0], node[1]+1])
            return


        # use dfs to do this
        # we will use dfs to do thi
        for row in range(len(heights)):
            dfs(atlantic, [row,len(heights[0])-1])
            dfs(pacific, [row, 0])
        for column in range(len(heights[0])):
            dfs(atlantic, [len(heights)-1, column])
            dfs(pacific, [0, column])

        final = atlantic.intersection(pacific)
        return list([list(i) for i in final ])        