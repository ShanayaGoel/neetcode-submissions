class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        app1 = {}
        app2 = {}
        s1 = list(s)
        t1 = list(t)
        for i in s1:
            if i in app1:
                app1[i] +=1
            else:
                app1[i] = 1
        for i in t1:
            if i in app2:
                app2[i] +=1
            else:
                app2[i] = 1

        for i in app1:
            if i not in app2:
                return False
            elif app2[i] != app1[i]:
                return False
        return True
        


        