# %%

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        maxC = max(candies)
        result = []
         
        for kid in candies:
            if kid + extraCandies >= maxC:
                result.append(True)
            else:
                result.append(False)
                



# %%

