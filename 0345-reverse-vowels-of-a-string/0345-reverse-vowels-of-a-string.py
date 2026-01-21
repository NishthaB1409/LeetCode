class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        chars = list(s)

        # collect vowels
        vocc = []
        for c in chars:
            if c in vowels:
                vocc.append(c)

        # replace vowels in reverse order
        ind = len(vocc) - 1
        for i in range(len(chars)):
            if chars[i] in vowels:
                chars[i] = vocc[ind]
                ind -= 1

        return "".join(chars)

        
        return s
            