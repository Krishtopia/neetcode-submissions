class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Practice timeeeeee - 19 OCT
        my_set = set(nums)
        longest = 0

        # Ex. my_set now's = {6,5,4,3,2}. Output should be: 5
        for num in my_set:
            if num-1 not in my_set:
                current = num
                length = 1
                
                while current+1 in my_set:
                    current += 1
                    length += 1
                
                longest = max(longest, length)
        return longest






















        # my_set = set(nums)
        # longest = 0

        # for num in my_set:
        #     if num - 1 not in my_set:
        #         current = num
        #         length = 1

        #         while current + 1 in my_set:
        #             current += 1
        #             length += 1

        #         longest = max(longest, length)

        # return longest