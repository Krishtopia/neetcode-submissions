class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        answer = []

        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in my_dict:
                answer.append(my_dict[needed])
                answer.append(i)
                return answer
            
            my_dict[nums[i]] = i
            