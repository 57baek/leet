# %%

from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]):

        hashMap = {}

        for num in arr:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1

        hashSet = set()

        flag = True

        for count in hashMap.values():
            if count in hashSet:
                flag = False
                break
            else:
                hashSet.add(count)

        return flag


# %%
sol = Solution()
print(sol.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))


# %%
class Solution(object):
    def uniqueOccurrences(self, arr):

        # A dictionary (or hash map) is a data structure that stores key-value pairs. Each key is unique, and the value associated with the key can be accessed efficiently using the key.
        # Counting Frequency (Dictionary):
        # The dictionary hashMap is used to count how many times each element in the array occurs. This concept is often referred to as frequency counting.
        # Initialize an empty dictionary (hashMap) to store the count of each element in arr
        hashMap = {}

        # Loop through each element in the input array arr
        for num in arr:
            # If the element num is already a key in the hashMap, increment its count
            if num in hashMap:
                hashMap[num] += 1
            # If the element num is not a key, add it to hashMap with a count of 1
            else:
                hashMap[num] = 1

        # A set is an unordered collection of unique elements. In a set, duplicates are automatically discarded.
        # Uniqueness Check (Set):
        # The set hashSet ensures that all occurrence counts are unique. This leverages the set’s property of storing only unique elements.
        # Initialize an empty set (hashSet) to track the unique counts of occurrences
        # For this code, set is used because it is efficient when look-up (List = O(n), set = O(1), dic = O(1)) not becasue it has uniqueness feature
        hashSet = set()

        # Initialize a flag variable as True. This will be used to indicate whether
        # all occurrences are unique or not.
        flag = True

        # Loop through the count of occurrences (values) in hashMap
        for count in hashMap.values():
            # If the count already exists in hashSet, it means the count is not unique
            if count in hashSet:
                # Set flag to False to indicate a repeated count and break the loop
                flag = False
                break
            # Otherwise, add the count to hashSet to keep track of it
            else:
                hashSet.add(count)

        # After checking all counts, return the value of flag
        # True if all occurrence counts are unique, False otherwise
        return flag
