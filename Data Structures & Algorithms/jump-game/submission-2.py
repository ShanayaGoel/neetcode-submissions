class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums) - 1
        goal = last_index
        for i in range(len(nums) -2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        if goal == 0:
            return True
        else:
            return False