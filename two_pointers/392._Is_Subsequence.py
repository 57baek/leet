# %%


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        s_len = len(s)
        t_len = len(t)

        sl = list(s)
        tl = list(t)

        i = 0
        s_i = 0
        count = 0

        if s_len == 0:
            return True

        while i < t_len:

            if sl[s_i] == tl[i]:
                s_i += 1
                count += 1

            if count == s_len:
                return True

        i += 1

        return False


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i, j = 0, 0

        while i < len(s) and j < len(t):

            if s[i] == t[j]:
                i += 1

            j += 1

        return i == len(s)


# %%
sol = Solution()
s = "abc"
t = "axbxxcx"
result = sol.isSubsequence(s, t)
print(result)

# %%


class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:

        i, j = 0, 0

        while i < len(s) and j < len(t):

            if s[i] == t[j]:

                i += 1

            j += 1

        return i == len(s)
