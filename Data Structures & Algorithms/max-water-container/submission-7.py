class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # set left and right pointers to the ends
        left = 0
        right  = len(heights) - 1
        #max var
        max = min(heights[left], heights[right])*(right-left)
        # use while loop while left < right where we keep checking which bar is smaller and move that
        while left < right :

            # ccheck if new water is greater than old max
            if  min(heights[left], heights[right])*(right-left) > max:
                max = min(heights[left], heights[right])*(right-left)
            # move smaller bar and update max
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        #return max
        return max
            
            
                
