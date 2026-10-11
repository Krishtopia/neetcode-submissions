class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # WEEKLY PRACTICE - 11 OCT 2026
        if len(s) != len(t):
            return False
        
        count = [0]*26 # irrespective of no. of n's it'll remain same so 0(1)
        for char in s:
            # let's find out the index
            index = ord(char) - ord("a")

            # append by +1 everytime you encounter a word
            count[index] += 1
        
        for char in t:
            # same step as the s!!!!!!!! with some difference
            index = ord(char) - ord("a")

            # we'll minus 1 everytime we encounter the character 
            count[index] -= 1
            
            # now we'll check if the given value at the index is less than 0
            if count[index] < 0:
                return False
        
        return True













        # if len(s) != len(t):
        #     return False
        # alphabet_counter = [0]*26
        # for char in s:
        #     index = ord(char) - ord("a")
        #     alphabet_counter[index] += 1
        
        # for char in t:
        #     index = ord(char) - ord("a")
        #     alphabet_counter[index] -= 1
        #     if alphabet_counter[index] < 0:
        #         return False
        # return True