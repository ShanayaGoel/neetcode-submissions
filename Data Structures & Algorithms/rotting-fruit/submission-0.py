class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # set minutes variable
        mins = 0
        # we will probably use breadth first search to find time for all the rotten fruit

        # set of fresh tuples
        fresh = set()
        # current rotten
        rotten = set()

        # next rotten set
        next_rotten = set()

        #populate these sets
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    fresh.add((r,c))
                elif grid[r][c] == 2:
                    rotten.add((r,c))

        # while loop until current rotten is empty
        while len(rotten) > 0 and len(fresh) > 0:
            
            # for each item in current rotten, visit all the neigbors that are in fresh and add to next rotten and remove from fresh 
            for fruit in rotten:
                r = fruit[0]
                c = fruit[1]
                if r > 0:
                    # check up
                    if (r-1, c) in fresh:
                        next_rotten.add((r-1, c))
                        fresh.remove((r-1, c))
                if r < len(grid) - 1:
                    # check down
                    if (r+1, c) in fresh:
                        next_rotten.add((r+1, c))
                        fresh.remove((r+1, c))
                if c > 0:
                    # check left
                    if (r, c-1) in fresh:
                        next_rotten.add((r, c-1))
                        fresh.remove((r, c-1))
                if c < len(grid[r]) - 1:
                    #check right
                    if (r, c+1) in fresh:
                        next_rotten.add((r, c+1))
                        fresh.remove((r, c+1))
            # +1 to minutes
            mins += 1
            # current rotten is now next rotten
            rotten = next_rotten
            # next rotten is now set()
            next_rotten = set()
        # now that while loop is finished, we know current rotten must be empty
        # if there are still fruits in fresh, return -1
        if len(fresh) > 0:
            return -1
        # else, return minutes
        else:
            return mins