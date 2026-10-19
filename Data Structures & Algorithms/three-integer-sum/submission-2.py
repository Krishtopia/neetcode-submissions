class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Practiceeeeee timemeeeeeee!!!!!!!!

        result = []
        nums.sort()

        for current_index, current_num in enumerate(nums):
            if current_num > 0:
                break
            
            if current_index > 0 and current_num == nums[current_index-1]:
                continue
            
            left = current_index + 1
            right = len(nums) - 1

            while left < right:
                total = current_num + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    result.append([current_num, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return result


















        # # let's pulll this off again

        # # we started with the result as a empty list, obvio to return it in the end.
        # result = []

        # # now come's the sorting part we have to sort the nums inorder for us to be sure that moving left towards larger value and moving right towards smaller..
        # nums.sort()

        # # and here we go with the usual condition:
        # for c_i, c_n in enumerate(nums):
        #     # if current number is nmore than 0 there's no point checking it, as the sum of 3 woudn't be equals to 0, so we'll break it as all the upcoming numbers will be larger (as we sort the nums out already).
        #     if c_n > 0:
        #         break

        #     # we have to check if current number ain't equals to the prev current, it might leads to duplicate so yeah!
        #     if c_i > 0 and c_n == nums[c_i-1]:
        #         continue
            

        #     l = c_i + 1 # left
        #     r = len(nums)-1 # right 

        #     # comes while loop as long as left < right for the current iteration!!!!!!
        #     while l < r:
        #         total = c_n + nums[l] + nums[r]

        #         # if total is less than 0 that means something negative so think what we need to do?? ofc to increase the left (remember left (to right) --> == increasing, right (to left) <---- == decreasing)
        #         if total > 0:
        #             r -= 1

        #         elif total < 0:
        #             l += 1

        #         else: # we append and += left and -= right for the next iteration to find another possible pair.
        #             result.append([c_n, nums[l], nums[r]])
        #             l += 1
        #             r -= 1
                    
        #             # let's checkout if the prev l is == to current l
        #             # if nums[l] == nums[l-1]:
        #             #     left += 1
        #             # but. but. but we can't what if left == right now we can't possibly do left += 1 + what if there are multiple's 1, 1, 1, 1 ??? we have to skip them all as well, means a while loop can be helpful with the condition while left < right as a stoppage so we can't go further than the current right index...
            
        #             # let's do this instead
        #             while l < r and nums[l] == nums[l-1]:
        #                 l += 1
        # return result












        # # result = []
        # # nums.sort()

        # # for current_index, current_number in enumerate(nums):
        # #     if current_number > 0:
        # #         break

        # #     if current_index > 0 and current_number == nums[current_index - 1]:
        # #         continue

        # #     left = current_index + 1
        # #     right = len(nums) - 1

        # #     while left < right:
        # #         total = current_number + nums[left] + nums[right]

        # #         if total > 0:
        # #             right -= 1
        # #         elif total < 0:
        # #             left += 1
        # #         else:
        # #             result.append([current_number, nums[left], nums[right]])
        # #             left += 1
        # #             right -= 1

        # #             while left < right and nums[left] == nums[left - 1]:
        # #                 left += 1

        # # return result

