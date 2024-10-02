# %%

"""

1.	Growing the Window (Expanding):
	•	As long as we encounter 1s in the array (nums[r] == 1), the subarray can keep growing. 
    •	No need to flip anything, so we just extend the right pointer (r).
	•	When we encounter a 0, we can still grow the subarray by flipping it into a 1 (by decreasing k).

2.	Maintaining the Size:
	•	If we have flipped exactly k 0s, the subarray has reached its maximum size while meeting the condition of at most k 0 flips.
	•	When we encounter another 0 (making k < 0), we can no longer maintain the current window size. 
    •	At this point, we need to shrink the window from the left by moving the left pointer (l), ensuring that we return to having at most k flipped zeroes.

3.	Shrinking the Window (Contracting):
	•	When k becomes negative (i.e., we have flipped more than k zeroes), 
    •	we shrink the window from the left until the number of zeroes flipped is again within the allowed limit (i.e., k >= 0).
	•	This is done by moving the left pointer (l), and if we pass over a 0, we “unflip” it by incrementing k.
    •   When nums[left] == 0, it means that 0, which was part of the subarray, is no longer part of it and thus we can increase the k.

"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        l = 0  # Initialize left pointer
        r = 0  # Initialize right pointer

        # Right pointer moves from the beginning to the end of the list
        for r in range(len(nums)):

            if nums[r] == 0:  # If the current element is 0
                k -= 1  # Decrease k because we're allowed to flip at most k zeroes

            if k < 0:  # If we've flipped more than k zeroes
                if nums[l] == 0:  # If the leftmost element of the window is 0
                    k += 1  # Revert the flip by moving left pointer, making one flip available again
                l += 1  # Shrink the window from the left to maintain at most k zeroes in the window

        # Return the length of the longest subarray that satisfies the condition
        return r - l + 1


# Test the solution
sol = Solution()
nums = [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
k = 2
print(sol.longestOnes(nums, k))  # Output should be 6
