class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_count = {}
        count = 0
       
        for i in s:
            char_count[i]=char_count.get(i,0) + 1
            
            count += 1

        for i in t:
            if i in char_count and char_count[i] > 0:
                char_count[i] -= 1
                count -= 1

        return count == 0