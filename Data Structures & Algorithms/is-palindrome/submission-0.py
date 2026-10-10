class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we're going to use 2 pointer technique here, left will iterate from the left side and right on the right side

        left = 0 # let's name it left_index ND right index!!!! ahh let it be it doesn't look good on the first while condition side
        right = len(s)-1

        # going to enter a while loop with condition as long as left is smaller than the right hand side the moment it false.. well yknow the rest....

        while left < right:
            # again we used left<right to prevent cases like these: "r!!!"... or "!!!!"

            while left < right and not s[left].isalnum():
                left += 1
            
            while left < right and not s[right].isalnum():
                right -= 1

                # on the left side we'll increment it and on the right we'll decrement by 1

            # COMPARISION TIMEEEEEE
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -=1
        return True