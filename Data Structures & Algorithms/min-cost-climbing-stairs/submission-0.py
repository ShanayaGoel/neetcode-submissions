class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = []
        n = len(cost)
        a.append(0)
        a.append(0)
        for i in range(2, n + 1):
            a.append(min(a[i-1] + cost[i-1], a[i-2] + cost[i-2] ))
        print(a)
        return a[n]