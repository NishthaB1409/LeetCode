class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapST, mapTS = {}, {}

        words = s.split()

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            c1, c2 = pattern[i], words[i]

            if (c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
                return False

            mapST[c1] = c2
            mapTS[c2] = c1

        return True
