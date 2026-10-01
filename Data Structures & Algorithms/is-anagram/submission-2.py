class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alphabet_counter = [0]*26
        for char in s:
            index = ord(char) - ord("a")
            alphabet_counter[index] += 1
        
        for char in t:
            index = ord(char) - ord("a")
            alphabet_counter[index] -= 1
            if alphabet_counter[index] < 0:
                return False
        return True