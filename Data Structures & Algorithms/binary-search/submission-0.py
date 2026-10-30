class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        if len(nums) == 0:
            return -1     
        middle = len(nums)//2
        if target < nums[middle]:
            val = self.search(nums[0:middle], target)
            if val == -1:
                return -1
            else:
                return val
        else:
            val = self.search(nums[middle:len(nums)], target)
            if val == -1:
                return -1
            else:
                return val + middle