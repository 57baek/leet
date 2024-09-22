# %%

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        if len(nums) < 3:
            return False

        # Two variables, first and second, are initialized to positive infinity (float('inf'))
        first = second = float("inf")

        for num in nums:
            if num <= first:
                first = num  # Update the smallest so far
            elif num <= second:
                second = num  # Update the second smallest so far
            else:
                return True  # We found a number larger than both

        return False


# %%

sol = Solution()
# nums = [1, 2, 3, 4]
nums = [2, 3, -2, -3]
# nums = [20, 100, 10, 12, 5, 13]
result = sol.increasingTriplet(nums)
print(result)
