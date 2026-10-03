class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        # let's track out POL(product of everything on the left hehee...)
        left_product = 1

        for i in range(len(nums)):
            answer[i] = left_product
            left_product *= nums[i]

        # now come's POR (product of everything to the righty....)
        right_product = 1

        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        # && here's your official answer is!!!!!!
        return answer