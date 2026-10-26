class Solution:
    def countBits(self, n: int) -> List[int]:
        count = []
        for num in range(n+1):
            count.append( bin(num).count("1"))
        return count