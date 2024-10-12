# %%

from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        n = len(grid)
        result = 0

        for i in range(n):
            row = grid[i]
            for j in range(n):

                # map(function, iterable) is a built-in Python function that applies a given function (function) to each item in an iterable (like a list, tuple, etc.) and returns an iterator.
                # row refers to each element (each row) of the grid as the map() function iterates over the grid
                col = list(map(lambda row: row[j], grid))

                if row == col:
                    result += 1

        return result


# %%
grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
sol = Solution()
print(sol.equalPairs(grid))

# %%

"""

lambda functions are commonly used with higher-order functions that expect a function as an argument, such as:

	•	map()
	•	filter()
	•	reduce()

# Doubling each number in a list
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))  # [2, 4, 6, 8]

# Filtering out even numbers
numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))  # [1, 3, 5]

# Sorting a list of tuples by the second element
data = [(1, 2), (3, 1), (5, 0)]
sorted_data = sorted(data, key=lambda x: x[1])  # [(5, 0), (3, 1), (1, 2)]

"""


# %%
class Solution:

    def equalPairs(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)

        for i in range(n):
            row = ",".join(map(str, grid[i]))

            for j in range(n):
                col = ",".join(str(grid[k][j]) for k in range(n))

                if col == row:
                    res += 1

        return res


# %%
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        m = defaultdict(int)
        cnt = 0

        for row in grid:
            m[str(row)] += 1

        for i in range(len(grid[0])):
            col = []

            for j in range(len(grid)):
                col.append(grid[j][i])

            cnt += m[str(col)]

        return cnt
