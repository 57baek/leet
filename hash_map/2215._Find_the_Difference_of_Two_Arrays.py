# %%

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        s1, s2 = set(nums1), set(nums2)

        result = [[], []]

        for i in s1:
            if i not in s2:
                result[0].append(i)

        for j in s2:
            if j not in s1:
                result[1].append(j)

        return result


# %%

sol = Solution()
print(sol.findDifference([1, 2, 3], [2, 4, 6]))

# %%


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        set1, set2 = set(nums1), set(nums2)

        return [list(set1 - set2), list(set2 - set1)]
