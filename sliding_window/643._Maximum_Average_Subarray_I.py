# %%

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        currentSum = maxSum = sum(nums[:k])

        for i in range(k, len(nums)):

            currentSum += nums[i] - nums[i - k]

            maxSum = max(maxSum, currentSum)

        return maxSum / k


# %%

sol = Solution()
nums = [1, 12, -5, -6, 50, 3]
result = sol.findMaxAverage(nums, 4)
print(result)


# %%


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # Initialize currSum and maxSum to the sum of the initial k elements
        currSum = maxSum = sum(nums[:k])

        # Start the loop from the kth element
        # Iterate until you reach the end
        for i in range(k, len(nums)):

            # Subtract the left element of the window
            # Add the right element of the window
            currSum += nums[i] - nums[i - k]

            # Update the max
            maxSum = max(maxSum, currSum)

        # Since the problem requires average, we return the average
        return maxSum / k