class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for n in range(0, len(nums)):
            if nums[n] not in map:
                map[nums[n]] = n
        
        for num in range(0, len(nums)):
            if ( target - nums[num] ) in map and map[ target - nums[num]] != num:
                return [min(map[target - nums[num]], num), max(map[target - nums[num]], num)]
                
        