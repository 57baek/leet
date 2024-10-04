# %%

from typing import List


class Solution:
    def largestAltutude(self, gain: List[int]) -> int:

        sum = 0
        maxSum = 0
        for alt in gain:
            sum += alt
            maxSum = max(sum, maxSum)
        return maxSum


# %%

sol = Solution()
print(sol.largestAltutude([-5, 1, 5, 0, -7]))
