# %%


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # 1) check whether there exist common divisor
        if str1 + str2 != str2 + str1:
            return ""

        # 2) get the common divisor using %
        l1, l2 = len(str1), len(str2)

        # Implementation of Euclid's Algorithms - Order does not matter / % gives whatever that is left
        """
        18 / (48) = 0 ... (18)
        48 / (18) = 2 ... (12)
        18 / (12) = 1 ... (6)
        12 / (6) = 2 ... (0) 
        GCD = 6
        """
        # while l2 is not 0 (can be negative or positive but not zero)
        while l2:
            l1, l2 = l2, l1 % l2

        # return str1 index 0 to l1
        return str1[:l1]


# %%

solution = Solution()

str1 = "ABAB"
str2 = "ABABABAB"

result = solution.gcdOfStrings(str1, str2)
print(result)

# %%

from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # Check if concatenated strings are equal or not, if not return ""
        if str1 + str2 != str2 + str1:
            return ""

        # If strings are equal than return the substring from 0 to gcd of size(str1), size(str2)
        return str1[: gcd(len(str1), len(str2))]


# end
