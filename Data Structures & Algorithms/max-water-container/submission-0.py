class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # i might've pulled this off, but gotta understand it again to get it lol. so... tomorrow, gonna give it another attempt!!!!    
        
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height

            max_area = max(max_area, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area