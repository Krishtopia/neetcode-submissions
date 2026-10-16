class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # let's try this out even though sliding window still feels a little confusing/but practice makes man perfect right hehee...

        # rn keeping track of the characters in our current substring using set()
        char_set = set()

        # so here left marks where our current substring starts
        left = 0

        # let's track of the longest substring we've found so far
        longest = 0

        # right moves forward, checking each character one by one
        for right in range(len(s)):

            # now the confusing part...
            # what if we find a character that's already in our set??
            while s[right] in char_set:

                # gotta remove the character at the left
                # so we can get rid of the duplicate
                char_set.remove(s[left])

                # move the start of our substring forward
                left += 1

            # no duplicate now, so let's add the current character
            char_set.add(s[right])

            # calculate the current substring's length...
            # right - left + 1 because both ends are included and update longest if we found a bigger one
            longest = max(longest, right - left + 1)

        # returning the longest substring length we found
        # will revisit tomorrow and try to pull it off againnn....
        return longest