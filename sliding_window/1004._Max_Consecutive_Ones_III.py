# %%

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        l = 0  # Initialize left pointer
        r = 0  # Initialize right pointer

        # Right pointer moves from the beginning to the end of the list
        for r in range(len(nums)):

            if nums[r] == 0:  # If the current element is 0
                k -= 1  # Decrease k because we're allowed to flip at most k zeroes

            if k < 0:  # If we've flipped more than k zeroes
                if nums[l] == 0:  # If the leftmost element of the window is 0
                    k += 1  # Revert the flip by moving left pointer, making one flip available again
                l += 1  # Shrink the window from the left to maintain at most k zeroes in the window

        # Return the length of the longest subarray that satisfies the condition
        return r - l + 1


# Test the solution
sol = Solution()
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
print(sol.longestOnes(nums, k))  # Output should be 6
