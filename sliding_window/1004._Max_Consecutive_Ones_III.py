# %%

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        maxCount = 0

        for i in range(len(nums)):

            tempK = k
            j = i
            count = 0

            while nums[j] == 1 or tempK > 0:

                if nums[j] == 1:
                    count += 1
                    j += 1

                else:
                    j += 1
                    count += 1
                    k -= 1

                maxCount = max(count, maxCount)

        return maxCount


# %%

sol = Solution()
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
print(sol.longestOnes(nums, k))


# %%

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        left = 0
        maxCount = 0
        tempK = k

        for right in range(len(nums)):
            # If we encounter a zero, decrease tempK
            if nums[right] == 0:
                tempK -= 1

            # If tempK drops below 0, move the left pointer
            while tempK < 0:
                if nums[left] == 0:
                    tempK += 1
                left += 1

            # Calculate the maximum length of the subarray
            maxCount = max(maxCount, right - left + 1)

        return maxCount


# Test the solution
sol = Solution()
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
print(sol.longestOnes(nums, k))  # Output should be 6
