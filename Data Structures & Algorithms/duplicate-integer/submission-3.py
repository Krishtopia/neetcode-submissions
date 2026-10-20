class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()

        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
        return False












        # WEEKLY PRACTICE TIME - 18 OCT
        my_set = set()

        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
        return False























        # my_set = set()
        # for num in nums:
        #     if num in my_set:
        #         return True
        #     my_set.add(num)
        # return False