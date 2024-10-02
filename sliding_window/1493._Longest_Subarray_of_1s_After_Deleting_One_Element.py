# %%

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        left = 0
        count = 1  # The number of 0's you are allowed to encounter (since you're allowed to delete 1)
        max_len = 0  # To track the maximum length

        for right in range(len(nums)):
            if nums[right] == 0:
                count -= 1

            # If count is negative, move the left pointer to the right to adjust the window
            while count < 0:
                if nums[left] == 0:
                    count += 1
                left += 1

            # Update the maximum length, exclude one element as we must delete exactly one 0
            max_len = max(max_len, right - left)

        return max_len


# %%

sol = Solution()
nums = [1, 1, 0, 1]
print(sol.longestSubarray(nums))  # Expected output: 3
