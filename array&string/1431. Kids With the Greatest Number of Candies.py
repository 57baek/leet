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
    
        return result 


# %%

solution = Solution()

candies = [2,3,5,1,3]
extraCandies = 3

result = solution.kidsWithCandies(candies, extraCandies)
print(result)


# %%

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [True if (c + extraCandies) >= max(candies) else False for c in candies]
        
