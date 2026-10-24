class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # max initialized
        max = 0
        # initialize left 
        left = 0
        #window is just 1
        # keep moving right to the right
        curr_set = set()
        
        for right in range(0, len(s)):
            # if right is equal to left, move left to the right
            while s[right] in curr_set and left != right:
                
                curr_set.remove(s[left])
                left += 1
            # else, if right-left > than max
            if right-left + 1 > max:
                    max = right-left + 1
            curr_set.add(s[right])


        # return max
        return max