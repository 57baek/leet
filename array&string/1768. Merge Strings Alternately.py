# %%
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        result = []
        arrLeng = max(len(word1), len(word2))
        
        # if arrLeng is 5, i will iterate 0 to 4
        for i in range(arrLeng):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
    
        return ''.join(result)

# %%
solution = Solution()

word1 = 'abc'
word2 = '12345'

result = solution.mergeAlternately(word1, word2)
print(result)

# %%
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        return ''.join(result)