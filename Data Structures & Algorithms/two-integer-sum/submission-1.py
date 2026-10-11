class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # WEEKLY PRACTICE 11 OCT!
        
        # why not set? well, we're going to return the index so yeah using dictionary would be better to hold the num as key and it's index as value 
        my_dict = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in my_dict:
                return [my_dict[needed], i]
            
            my_dict[nums[i]] = i
        return False



















        # my_dict = {}
        # answer = []

        # for i in range(len(nums)):
        #     needed = target - nums[i]
        #     if needed in my_dict:
        #         answer.append(my_dict[needed])
        #         answer.append(i)
        #         return answer
            
        #     my_dict[nums[i]] = i
            