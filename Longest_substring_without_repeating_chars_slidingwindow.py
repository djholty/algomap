class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        n = len(s)
        max_window = 0
        sett = set()

        for r in range(n):
            
            while s[r] in sett:
                sett.remove(s[left])
                left += 1
            sett.add(s[r])
            window = (r - left) + 1
            max_window =  max(max_window, window)
        
        return max_window
