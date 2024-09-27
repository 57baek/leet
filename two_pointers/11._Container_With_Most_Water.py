# %%

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = 0
        i = 0
        j = len(height) - 1

        while i < j:

            current_area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, current_area)

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return max_area


# %%

sol = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = sol.maxArea(height)
print(result)


# %%


class Solution2:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:

            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea
