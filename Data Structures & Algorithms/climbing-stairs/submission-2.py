class Solution:
    def climbStairs(self, n: int) -> int:
        opt = [0] * (n+1)
        opt[0] = 1
        for i in range(0, n):
            opt[i+1] += opt[i]
            if i < n-1:
                opt[i+2] += opt[i]
        return opt[n]

        