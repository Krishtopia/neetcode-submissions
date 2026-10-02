class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}

        # let's try to count the frequencies
        for num in nums:
            my_dict[num] = my_dict.get(num, 0) + 1

        # on my way to ~ sorting it
        sorted_items = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

        # take the first k numbers....
        return [item[0] for item in sorted_items[:k]]