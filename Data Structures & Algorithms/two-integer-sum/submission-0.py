class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for n in range(0, len(nums)-1):
            diff = target - nums[n]
            for n2 in range(n+1, len(nums)):
                if diff == nums[n2]:
                    return[n,n2]