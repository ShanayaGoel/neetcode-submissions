class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        freq = [set() for _ in range(len(nums)+2)]
        max = 0
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] +=1
            if seen[num] > max:
                max = seen[num]
        for num in seen:
            freq[seen[num]].add(num)
        most_freq = []
        for i in range(max, 0, -1):
            most_freq += list(freq[i])
            if len(most_freq) == k:
                return most_freq
        