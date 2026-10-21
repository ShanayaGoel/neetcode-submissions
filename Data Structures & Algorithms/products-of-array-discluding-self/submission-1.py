class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = []
        right = [1] * len(nums)
        # array to be returned
        array_tbr = []

        left.append(1)

        for i in range(1, len(nums)):
            left.append(left[i-1]* nums[i-1])
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1]*nums[i+1]
        for n in range(0, len(nums)):
            array_tbr.append(left[n]*right[n])
        return array_tbr