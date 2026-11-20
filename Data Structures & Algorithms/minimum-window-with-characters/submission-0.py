class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        # first let's count the frequency of each character in t
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        window = {}

        left = 0
        have = 0
        need = len(count_t)

        result = [-1, -1]
        result_length = float("inf")

        for right in range(len(s)):
            # now we need to expand the window by adding the new character
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # let'd check if this character satisfies its required frequency
            if char in count_t and window[char] == count_t[char]:
                have += 1

            # shrink the window while all required characters are satisfied
            while have == need:
                window_length = right - left + 1

                # now update the minimum window if this one is shorter
                if window_length < result_length:
                    result = [left, right]
                    result_length = window_length

                # remove the leftmost character from the window
                left_char = s[left]
                window[left_char] -= 1

                # check if removing this character breaks a requirement
                if left_char in count_t and window[left_char] < count_t[left_char]:
                    have -= 1

                left += 1

        left, right = result

        return s[left:right + 1] if result_length != float("inf") else ""