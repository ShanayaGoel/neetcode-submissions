class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        st = {}
        for s in strs:
            s2 = list(s)
            s3 = tuple(sorted(s2))
            if s3 in st:
                st[s3].append(s)
            else:
                st[s3] = [s]
        new_l = [st[i] for i in st]
        return(new_l)