class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        break_here = [False] * (n+1)
        break_here[0] = True
        for i in range(1, n + 1):
            for word in wordDict:
                if len(word) <= i :
                    if s[(i-len(word)) : i] == word and break_here[i - len(word)] == True:
                        break_here[i] = True
        return break_here[n]
        