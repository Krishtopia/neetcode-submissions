class Solution:
    def trap(self, height: List[int]) -> int:
        # let's try to pull this off even though tbh i am still confused
        # how exactly we are supposed to approach this problem lmao..
        # anyway....
        left = 0
        right = len(height) - 1

        # starting with both pointers at the ends of the array

        # let's set it out, the max of each (yup like a counter)
        left_max = 0
        right_max = 0
        total_water = 0

        # here comes the while loop, we keep going until left and right meet....

        # now the confusing part begins: how do we know which side to process nd why can we calculate the water w/o checking everything again?????
        while left < right:

            if height[left] < height[right]:

                # if the current left bar is >= the tallest left bar so far -->
                # we update left_max because we found a new tallest bar..
                if height[left] >= left_max:
                    left_max = height[left]

                else:
                    # otherwise, the current bar is smaller than left_max so apparently the difference is the water we can store
                    # i still need to understand ***WHY**** this is enough without
                    # checking every bar on the right myself...
                    total_water += left_max - height[left]

                left += 1

            else:
                # doing the same thing from the right side now.
                if height[right] >= right_max:
                    right_max = height[right]

                else:
                    # if the current bar is shorter than right_max.the difference is added to the total water.
                    total_water += right_max - height[right]

                right -= 1

        # returning the total water collected
        # got the code with help, but tomorrow we'llll go through it again
        # && try to understand the logic properly on my own
        return total_water