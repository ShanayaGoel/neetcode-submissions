class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while right > left:

            if s[right].isalnum() and s[left].isalnum():
                if s[right].upper() == s[left].upper():
                    right -= 1
                    left += 1
                else:
                    
                    return False
            elif s[right].isalnum():
                left += 1
            else:
                right -= 1
        return True
        