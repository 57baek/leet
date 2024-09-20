# %%
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []
        count = 0
        temp = 1
        
        while count < len(nums):
            for i in range(len(nums)):
                if i == count:
                    continue
                temp *= nums[i]
            result.append(temp)
            temp = 1
            count += 1
        
        return result
            
# %%

sol = Solution()
nums = [1,2,3,4]
result = sol.productExceptSelf(nums)
print(result)

# %%

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_product = 1
        postfix_product = 1
        result = [0] * len(nums)  # Initialize the result array with zeros

        '''
        [A, B, C, D]
        For the element at i = 1 (say B), we need to multiply prefix A and postfix C * D
        We are setting prefixes using the first loop and multiply postfixes using the second loop
        '''

        # First pass: compute prefix product for each element
        for i in range(len(nums)):
            result[i] = prefix_product   # At index i, store the product of all elements before i
            prefix_product *= nums[i]    # Update prefix product by multiplying with nums[i]

        # Second pass: compute postfix product and multiply with the current result
        for i in range(len(nums) - 1, -1, -1):  # Traverse the array backward
            result[i] *= postfix_product  # Multiply with the postfix product at index i
            postfix_product *= nums[i]    # Update postfix product by multiplying with nums[i]

        return result