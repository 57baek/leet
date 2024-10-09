# %%

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        cnt1 = Counter(word1)
        cnt2 = Counter(word2)

        sort1 = sorted(cnt1.values())
        sort2 = sorted(cnt2.values())

        length_frequency_match = sort1 == sort2
        character_match = set(cnt1.keys()) == set(cnt2.keys())

        return length_frequency_match and character_match


# %%
sol = Solution()
print(sol.closeStrings("cabbba", "abbccc"))


# %%
# Counter will take a string as input and return a dictionary-like object
# keys are the character
# values are the counts of how many times each character appears.
from collections import Counter

word1 = "abbccc"
frequency_word1 = Counter(word1)
print(frequency_word1)
# Counter({'c': 3, 'b': 2, 'a': 1})

# %%
# The sorted() function in Python takes an iterable (such as a list, set, or dictionary values)
# and returns a new list containing all elements sorted in ascending order (by default).
values = [3, 1, 2]
sorted_values = sorted(values)
print(sorted_values)
# [1, 2, 3]

# %%
# In Python, dictionaries have a .values() method that returns a view object containing all the values in the dictionary.
# You cannot directly index or sort a dictionary, so the .values() method is used to extract the values (in this case, the counts from Counter) into a format that can be sorted or compared.
frequency_word1 = Counter("abbccc")
values_word1 = frequency_word1.values()
print(values_word1)
# dict_values([1, 2, 3])

# %%
# In Python, dictionaries have a .keys() method that returns a view object containing all the keys of the dictionary. In the case of the Counter object, the keys represent the unique characters from the input string.
frequency_word1 = Counter("abbccc")
keys_word1 = frequency_word1.keys()
print(keys_word1)
# dict_keys(['a', 'b', 'c'])

# %%
# A set in Python is an unordered collection of unique elements. Sets are useful for quickly comparing or checking if two collections have the same elements, without caring about their order.
# The code uses set() to get the unique characters (the dictionary keys) from the frequency counters. It compares the sets of keys from both word1 and word2 to ensure that both words contain the exact same characters.
keys_word1 = set(Counter("abbccc").keys())
keys_word2 = set(Counter("bbaaccc").keys())
print(keys_word1 == keys_word2)
# True


# %%
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        frequency_word1 = Counter(word1)
        frequency_word2 = Counter(word2)

        # Check whether 1) Same Length and 2) Same Frequency Distribution (NOT checking whether same character)
        sorted_values_word1 = sorted(frequency_word1.values())
        sorted_values_word2 = sorted(frequency_word2.values())

        # Check whether the two strings have the same unique characters
        keys_match = set(frequency_word1.keys()) == set(frequency_word2.keys())

        return sorted_values_word1 == sorted_values_word2 and keys_match
