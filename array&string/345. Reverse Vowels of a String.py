# %%

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        s = list(s)
        right_index = len(s) - 1
        for leftV_index in range(len(s)):
            if s[leftV_index] in ('a', 'e', 'i', 'o', 'u'):
                temp_leftV = s[leftV_index]
            for rightV_index in range(right_index, -1, -1):
                if s[rightV_index] in ('a', 'e', 'i', 'o', 'u'):
                    s[leftV_index] = s[rightV_index]
                    s[rightV_index] = temp_leftV
                    right_index = rightV_index
        return ''.join(s)

# %%

sol = Solution()

s = "IceCreAm"
result = sol.reverseVowels(s)
print(result)