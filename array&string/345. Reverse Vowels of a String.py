# %%

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        # set works as unordered unique collection of elements -> {'o', 'E', 'e', 'O', 'I', 'i', 'u', 'A', 'U', 'a'}
        vowels = set('aeiouAEIOU')
        # list converts the string s into a list of characters. Since strings in Python are immutable (cannot be changed), converting it to a list allows us to swap characters directly
        # ['s', 't', 'r']
        s = list(s)
        left_index, right_index = 0, len(s) - 1
        
        while left_index < right_index:
            # Move the left pointer until we find a vowel
            # in 
            '''
        	•	Set: Best choice for large collections because it offers constant-time lookup (O(1)).
        	•	List/Tuple: Slower for large collections, but can still be used if performance is not a concern.
        	•	String: Works well when you're just checking characters, but less efficient than a set if you're doing frequent checks.
            For your vowel-reversal task, using a set is recommended because it provides faster membership checking compared to a list or tuple. However, any of the above collections can work depending on the use case.
            '''
            if s[left_index] not in vowels:
                left_index += 1
                # This skips the rest of the current iteration and goes back to the start of the while loop to check the next character from the left side.
                continue
                
            # Move the right pointer until we find a vowel
            if s[right_index] not in vowels:
                right_index -= 1
                continue
                
            # Swap the vowels at left_index and right_index
            s[left_index], s[right_index] = s[right_index], s[left_index]
            
            # Move both pointers inward
            left_index += 1
            right_index -= 1
        
        return ''.join(s)  # Convert list back to string

        
# %%

sol = Solution()

s = "IceCreAm"
result = sol.reverseVowels(s)
print(result)

# %%

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        '''     	
        •	List comprehension: This line uses a list comprehension to create a list vow that contains only the vowels from the string s.
	    •	c for c in s if c in vowels: For each character c in the string s, if the character is a vowel (i.e., if c in vowels is true), it is added to the vow list.
	    •	vow: After this step, vow will contain all the vowels from the original string, in the same order they appeared in s.
        '''
        vow = [c for c in s if c in vowels]
        revStr = []
        i = 0
        for char in s:
            if char in vowels:
                '''
            	•	if char in vowels: If the current character char is a vowel (i.e., it exists in the vowels string):
            	•	revStr.append(vow.pop()): Append the last vowel from the vow list (i.e., vow.pop()) to revStr. The pop() method removes and returns the last element of the list, which means you are appending the vowels in reverse order.
            	•	else: If the character is not a vowel:
            	•	revStr.append(char): Simply append the character to revStr as is.
                '''
                revStr.append(vow.pop())
            else:
                revStr.append(char)
        return ''.join(revStr)