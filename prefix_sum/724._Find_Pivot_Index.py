# %%

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        r = sum(nums)

        for i in range(len(nums)):
            r -= nums[i]

            if l == r:
                return i

            l += nums[i]

        return -1


# %%
sol = Solution()
print(sol.pivotIndex([1, 7, 3, 6, 5, 6]))
