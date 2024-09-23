# %%

# from typing import List

# class Solution:
#     def compress(self, chars: List[str]) -> int:
#
#         s = ""
#         pre_item = ""
#         count = 0
#         chars.append("X")
#
#         for i in range(len(chars)):
#
#             item = chars[i]
#
#             # initial
#             if pre_item == "":
#                 pre_item = item
#                 count += 1
#
#             elif pre_item == item:
#                 count += 1
#
#             else:
#
#                 if count == 1:
#                     s += pre_item
#
#                 elif count > 9:
#                     s += pre_item
#                     count_str = str(count)
#                     for count_char in count_str:
#                         s += count_char
#
#                 pre_item = item
#                 count = 1
#
#         return len(s)


"""
•	Use a for loop when:
    •	You have a clear, predefined sequence or range to iterate over.
    •	Each element needs to be processed once in a straightforward way.
    •	No complex control of the index is required.
•	Use a while loop when:
    •	The number of iterations isn’t known in advance (e.g., depends on conditions during execution).
    •	You need to manually control the index or the loop’s condition.
    •	Complex logic, such as skipping or revisiting elements, is needed.
    •	When another condition is required to run the loop

In this case, where we have to move index to specific point (a,a,a,b,b) 
-> after processing the group of a, we have to jump to the next group of b: use while loop
"""


# %%

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:

        ans = 0
        i = 0

        while i < len(chars):

            # current letter
            # reset count to 0
            letter = chars[i]
            count = 0

            # another loop until different letter shows up
            # come back to the original index when new letter shows up
            while i < len(chars) and chars[i] == letter:
                count += 1
                i += 1

            # append new letter to the result
            # move to the next index
            chars[ans] = letter
            ans += 1

            # returninig count if greater than 1
            if count > 1:

                for c in str(count):
                    chars[ans] = c
                    ans += 1

        return ans


# %%
sol = Solution()
chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
result = sol.compress(chars)
print(result)
