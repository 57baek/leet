# %%

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:

        s = ""
        pre_item = ""
        count = 0
        chars.append("X")

        for i in range(len(chars)):

            item = chars[i]

            # initial
            if pre_item == "":
                pre_item = item
                count += 1

            elif pre_item == item:
                count += 1

            else:

                if count == 1:
                    s += pre_item

                elif count > 9:
                    s += pre_item
                    count_str = str(count)
                    for count_char in count_str:
                        s += count_char

                pre_item = item
                count = 1

        return len(s)


# %%
sol = Solution()
chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
result = sol.compress(chars)
print(result)
