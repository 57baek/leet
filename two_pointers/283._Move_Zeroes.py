# %%

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        for i in range(len(nums)):

            if nums[i] == 0:

                j = i + 1
                while j < len(nums):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    j += 1


# %%

sol = Solution()
nums = [5, 6, 0, 0, 7, 8, 0, 9]
result = sol.moveZeroes(nums)
print(nums)


# %%

from typing import List


class Solution:
    def moveZeroes(self, nums):

        non_zero = 0  # Pointer for non-zero elements

        # Move all non-zero elements to the front
        for i in range(len(nums)):

            if nums[i] != 0:

                nums[i], nums[non_zero] = nums[non_zero], nums[i]
                non_zero += 1
