class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        new_g = grid.copy()
        count = 0


        def search( g: List[List[str]], x_val: int, y_val: int ) -> None:
            g[y_val][x_val] = "0"
            if y_val < (len(new_g)-1) and g[y_val + 1][x_val] == "1":
                search(g, x_val, y_val + 1 )
            if y_val > 0 and g[y_val - 1][x_val] == "1":
                search(g, x_val, y_val - 1 )
            if x_val < (len(new_g[y_val])-1) and g[y_val][x_val + 1] == "1":
                search(g, x_val + 1, y_val )
            if x_val > 0 and g[y_val][x_val - 1] == "1":
                search(g, x_val - 1, y_val)
            
        for y in range(0, len(new_g)):
            for x in range(0, len(new_g[y])):
                if new_g[y][x] == "1":
                    count += 1
                    print(x)
                    print(y)
                    search(new_g, x, y)
        return count

