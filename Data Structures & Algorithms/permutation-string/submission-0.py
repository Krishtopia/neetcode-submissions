class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # let's keep track of character frequencies
        s1_count = [0] * 26
        s2_count = [0] * 26

        # now now now count characters in s1 and the first window of s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        # check the first window
        if s1_count == s2_count:
            return True

        # slide the window through the remaining characters
        for right in range(len(s1), len(s2)):
            
            # add the new character entering the window
            s2_count[ord(s2[right]) - ord('a')] += 1

            # remove the character leaving the window
            left = right - len(s1)
            s2_count[ord(s2[left]) - ord('a')] -= 1

            # compare character frequencies
            if s1_count == s2_count:
                return True

        return False

        