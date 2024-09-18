# %%

class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)  # Convert string to list (not strictly necessary)
        word = []    # To build individual words
        result = []  # To store the resulting words
        
        for char in s:
            if char != ' ':  # If the character is not a space, build the word
                word.append(char)
            elif len(word) != 0:  # If a space is encountered and we have built a word
                result.append(''.join(word))  # Append the word to result
                word = []  # Clear the word to start fresh for the next word
        # If there is a word at the end without a trailing space
        if len(word) != 0:
            result.append(''.join(word))

        # Initialize two pointers, left starting from the beginning and right starting from the end
        left, right = 0, len(result) - 1
        # Loop until the two pointers meet in the middle
        while left < right:
            # Swap the elements at the left and right indices
            result[left], result[right] = result[right], result[left]
            # Move the left pointer one step to the right
            left += 1
            # Move the right pointer one step to the left
            right -= 1
        # After the list is reversed, join the words back into a single string with spaces between them
        return ' '.join(result)
# %%

sol = Solution()
s = "     a    ice     cream    "
result = sol.reverseWords(s)
print(result)
                
# %%

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Split the string into words
        words = s.split()
        
        # Reverse the list of words
        reversed_words = words[::-1]
        
        # Join the reversed words with spaces
        reversed_string = ' '.join(reversed_words)
        
        return reversed_string
    
# %%

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])                