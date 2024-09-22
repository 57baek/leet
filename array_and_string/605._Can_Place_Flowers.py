# %%

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if len(flowerbed) == 0:
            return False

        tempFlowerbed = flowerbed.copy()  # Avoid modifying the original list
        count = 0
        
        for i in range(len(tempFlowerbed)):
            
            # Check for the first spot
            if i == 0:
                # Check for the single-value list
                if len(tempFlowerbed) == 1:
                    if tempFlowerbed[0] == 0:
                        tempFlowerbed[0] = 1
                        count += 1
                elif tempFlowerbed[0] == 0 and tempFlowerbed[1] == 0:
                    tempFlowerbed[0] = 1
                    count += 1
            
            # Check for the last spot
            elif i == len(tempFlowerbed) - 1:
                if tempFlowerbed[-1] == 0 and tempFlowerbed[-2] == 0:
                    tempFlowerbed[-1] = 1
                    count += 1
            
            # Check for the middle spots
            elif tempFlowerbed[i] == 0 and tempFlowerbed[i - 1] == 0 and tempFlowerbed[i + 1] == 0:
                tempFlowerbed[i] = 1
                count += 1
        
        return count >= n
            
# %%

solution = Solution()
flowerbed = [0,0,0,0,0,1]
n = 2

result = solution.canPlaceFlowers(flowerbed, n)
print(result)

# %%

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    
        for i in range(len(flowerbed)):
            left = i == 0 or flowerbed[i-1] == 0
            right = i == len(flowerbed) - 1 or flowerbed[i+1] == 0

            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        
        return n <= 0

# end