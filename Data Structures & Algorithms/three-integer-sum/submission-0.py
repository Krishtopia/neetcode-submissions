class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for current_index, current_number in enumerate(nums):
            if current_number > 0:
                break

            if current_index > 0 and current_number == nums[current_index - 1]:
                continue

            left = current_index + 1
            right = len(nums) - 1

            while left < right:
                total = current_number + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    result.append([current_number, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result

