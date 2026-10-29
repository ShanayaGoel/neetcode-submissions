class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        freq = [set() for _ in range(len(nums)+2)]
        max = 0
        for num in nums:
            if num not in seen:
                seen[num] = 1
                freq[1].add(num)
            else:
                freq[seen[num]].remove(num)
                seen[num] +=1
                freq[seen[num]].add(num)
            if seen[num] > max:
                max = seen[num]
        most_freq = []
        for i in range(max, 0, -1):
            most_freq += list(freq[i])
            if len(most_freq) == k:
                return most_freq
        return most_freq
        