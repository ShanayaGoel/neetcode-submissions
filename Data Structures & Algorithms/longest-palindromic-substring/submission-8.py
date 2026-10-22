class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        max_pal = s[0]

        
        for c in range(0, len(s)):
            #even check
            if c+1 < len(s) and s[c] == s[c+1]:
                radius = 0
                while c-radius >= 0 and c+1+radius <len(s) and s[c-radius] == s[c+1+radius]:
                    radius += 1
                if radius*2 > max_len:
                    max_len = radius*2
                    max_pal = s[c-(radius-1): c+(radius-1) + 2]

            #odd check
            radius = 0

            while c-radius >=0 and c+radius <len(s) and s[c-radius] == s[c+radius]:
                radius += 1
            if radius*2 - 1 > max_len:
                max_len = radius*2 - 1
                max_pal = s[c-(radius-1): c+(radius-1) + 1 ]

        return max_pal