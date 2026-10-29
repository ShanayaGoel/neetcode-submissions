class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = {}
        ran_count = {}

        for c in magazine:
            if c in magazine_count:
                magazine_count[c] += 1
            else:
                magazine_count[c] = 1
        for c in ransomNote:
            if c in ran_count:
                ran_count[c] += 1
            else:
                ran_count[c] = 1
        for r in ran_count:
            if r not in magazine_count:
                return False
            elif magazine_count[r] < ran_count[r]:
                return False
        print(magazine_count)
        print(ran_count)
        
        return True