class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = []
        for s in strs:
            new_str.append(str(len(s)))
            new_str.append("#")
            new_str.append(s)
        return "".join(new_str)
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        list_tbr = []
        c1 = 0
        while c1 < len(s):
            c = c1
            while s[c] != "#":
                c += 1
            num = int(s[c1:c])
            c1 = c + 1
            c = c1 + num
            list_tbr.append(s[c1:c])
            c1 = c
        return list_tbr



