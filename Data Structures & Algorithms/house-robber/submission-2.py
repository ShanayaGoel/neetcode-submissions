class Solution:
    def rob(self, nums: List[int]) -> int:
        opt_rob = [0]*len(nums)
        # base case for first index
        opt_rob[0] = nums[0]
        if len(nums) == 1:
            return opt_rob[0]
        opt_rob[1] = max(nums[1], nums[0])
        if len(nums) == 2:
            return opt_rob[1]
        # dp step
        for house in range(2,len(nums)):
            opt_rob[house] = max(opt_rob[house-2] + nums[house], opt_rob[house-1])
        # return final value
        return opt_rob[len(nums)-1]


