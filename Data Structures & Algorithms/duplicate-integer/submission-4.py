class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appeared = set()
        for item in nums:
            if item in appeared:
                return True
            else:
                appeared.add(item)
        return False