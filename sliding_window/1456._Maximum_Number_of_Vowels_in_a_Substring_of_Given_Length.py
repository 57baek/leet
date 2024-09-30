# %%


class Solution:

    def maxVowels(self, s: str, k: int):

        vowel = set("aeiou")

        curCount = sum(1 for char in s[:k] if char in vowel)
        maxCount = curCount

        for i in range(k, len(s)):

            if s[i] in vowel:
                curCount += 1

            elif s[i - k] in vowel:
                curCount -= 1

            maxCount = max(maxCount, curCount)

        return maxCount


# %%


class Solution1:

    def maxVowels(self, s: str, k: int) -> int:

        # Define the set of vowels for faster lookup than List
        vowel = {"a", "e", "i", "o", "u"}

        # Initialize the count of vowels in the first k characters
        cur_vowel_count = 0

        # Count vowels in the initial substring of length k
        for char in s[:k]:
            if char in vowel:
                cur_vowel_count += 1

        # Initialize the maximum vowel count
        max_vowel_count = cur_vowel_count

        # Use a sliding window to move across the string
        for i in range(k, len(s)):
            # Remove the influence of the character that slides out of the window
            if s[i - k] in vowel:
                cur_vowel_count -= 1

            # Add the influence of the new character that slides into the window
            if s[i] in vowel:
                cur_vowel_count += 1

            # Update the maximum count of vowels if the current window has more vowels
            max_vowel_count = max(max_vowel_count, cur_vowel_count)

        return max_vowel_count


# %%


solution = Solution()
print(solution.maxVowels("abciiidef", 3))  # Output: 3


# %%


class Solution2:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set("aeiou")  # Use a set for faster lookup

        # Count the vowels in the first substring of length k
        cur_vowel_count = sum(1 for char in s[:k] if char in vowel)
        max_vowel_count = cur_vowel_count

        # Use a sliding window to check all subsequent substrings of length k
        for i in range(k, len(s)):
            # Remove the influence of the character that is sliding out of the window
            if s[i - k] in vowel:
                cur_vowel_count -= 1
            # Add the influence of the new character in the window
            if s[i] in vowel:
                cur_vowel_count += 1
            # Update the maximum count of vowels found so far
            max_vowel_count = max(max_vowel_count, cur_vowel_count)

        return max_vowel_count
