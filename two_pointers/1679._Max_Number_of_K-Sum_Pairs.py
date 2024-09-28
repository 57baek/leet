# %%

from typing import List


class Solution:
    def maxOperation(self, nums: List[int], k: int) -> int:

        # i = 0
        # j = len(nums) - 1
        #
        # small_half = range(k // 2)
        # small_half = list(small_half)
        # small_half = [elem + 1 for elem in small_half]
        #
        # large_half = [k - elem for elem in small_half]
        #
        # while i < j:

        nums.sort()

        i = 0
        j = len(nums) - 1
        count = 0

        while i < j:

            if nums[i] + nums[j] == k:
                count += 1
                i += 1
                j -= 1

            elif nums[i] + nums[j] < k:
                i += 1

            else:
                j -= 1

        return count


# %%

sol = Solution()
nums = [4, 7, 8, 9, 3, 2, 4, 6, 7, 1, 7, 8, 9, 1]
result = sol.maxOperation(nums, 7)
print(result)


# %%


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1
        operation = 0

        while left < right:
            if (nums[left] + nums[right]) == k:
                operation += 1
                left += 1
                right -= 1
            elif (nums[left] + nums[right]) < k:
                left += 1
            else:
                right -= 1
        return operation
