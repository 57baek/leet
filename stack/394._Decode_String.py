# %%


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            ## Keep adding to Stack until a ']'
            if char != "]":
                stack.append(char)

            else:
                ## Extracting SubString to be Multiplied
                curr_str = ""
                # stack[-1] indicates the element that will be popped
                while stack[-1] != "[":
                    curr_str = stack.pop() + curr_str
                ## Pop to remove '['
                stack.pop()

                ## Extract full number (handles multi-digit, e.g. 10)
                curr_num = ""
                while stack and stack[-1].isdigit():
                    curr_num = stack.pop() + curr_num

                ## Updating Stack with multiplied string
                curr_str = int(curr_num) * curr_str
                stack.append(curr_str)

        return "".join(stack)


# %%
sol = Solution()
s = "3[a2[c]]"
print(sol.decodeString(s))

"""

1) 3[a2[c
1-1) curr_str = c

2) 3[a2
2-1) curr_num = 2
2-2) curr_str = cc

3) 3[a
3-1) curr_str = acc

4) 3
4-1) curr_num = 3
4-2) curr_str = accaccacc

"""
