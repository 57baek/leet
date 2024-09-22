# %%

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        for index in range(len(nums) - 1, -1, -1):

            for sub_index in range(index, -1, -1):
                if nums[sub_index] < nums[index]:

                    for sub_sub_index in range(sub_index, -1, -1):
                        if nums[sub_sub_index] < nums[sub_index]:
                            return True

        return False


# %%

sol = Solution()
# nums = [1, 2, 3, 4]
nums = [2, 3, -2, -3]
# nums = [20, 100, 10, 12, 5, 13]
result = sol.increasingTriplet(nums)
print(result)
