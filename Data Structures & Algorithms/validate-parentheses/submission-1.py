class Solution:
    def isValid(self, s: str) -> bool:
        s2 = list(s)
        stk = []
        ls = 0
        for i in s2:
            if ls == 0:
                stk.append(i)
                ls += 1
            elif i == ")" and stk[ls-1] == "(" or i == "]" and stk[ls-1] == "[" or i == "}" and stk[ls-1] == "{" :
                stk.pop()
                ls -=1
            else:
                stk.append(i)
                ls += 1
        if ls != 0:
            return False
        return True
                
