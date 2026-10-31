class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for s in strs:
            new_str += str(len(s))
            new_str += "#"
            new_str += s
        return new_str
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        string = s
        list_tbr = []
        c = 0
        while string != "":
            c = 0
            num = ""
            str_new = ""
            while string[c] != "#":
                num += string[c]
                c += 1
            for n in range(int(num)):
                c += 1
                str_new += string[c]
            list_tbr.append(str_new)
            string = string[c + 1:]
        return list_tbr



