class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        #for counting frequency
        for c in s:
            freq[c] = freq.get(c, 0) + 1

        #finding unique character
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1
