# %%

from typing import List


class timSort:
    
    def insertionSort(self, nums:List[int], left: int, right: int) -> None:
        
                              


    def mergeSort(self, nums:List[int]) -> None:


    def timSort(self, nums:List[int]) -> List[int]:

        runSize = 4
        n = len(nums)

        for start in range(0, n, runSize):
            end = min(start + runSize - 1, n - 1)
            self.insertionSort(nums, start, end)















# %%

from typing import List


class TimSort:
    
    # Insertion sort for sorting small chunks
    def insertionSort(self, nums: List[int], left: int, right: int) -> None:
        for i in range(left + 1, right + 1):
            key = nums[i]
            j = i - 1
            # Move elements greater than the key to one position ahead
            while j >= left and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
    
    # Merge two sorted subarrays
    def merge(self, nums: List[int], left: int, mid: int, right: int) -> None:
        # Create temporary arrays
        left_half = nums[left:mid + 1]
        right_half = nums[mid + 1:right + 1]

        i = j = 0
        k = left

        # Merge the temp arrays back into nums
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                nums[k] = left_half[i]
                i += 1
            else:
                nums[k] = right_half[j]
                j += 1
            k += 1

        # Copy any remaining elements of left_half
        while i < len(left_half):
            nums[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements of right_half
        while j < len(right_half):
            nums[k] = right_half[j]
            j += 1
            k += 1
    
    # Timsort algorithm
    def timSort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        run_size = 4  # This is the chunk size we use for insertion sort

        # Step 1: Sort small chunks with insertion sort
        for start in range(0, n, run_size):
            end = min(start + run_size - 1, n - 1)
            self.insertionSort(nums, start, end)

        # Step 2: Merge sorted chunks using merge sort
        size = run_size
        while size < n:
            for left in range(0, n, 2 * size):
                mid = min(left + size - 1, n - 1)
                right = min((left + 2 * size - 1), n - 1)
                if mid < right:
                    self.merge(nums, left, mid, right)
            size *= 2
        
        return nums

# %% Example Usage:

nums = [5, 21, 7, 23, 19, 2, 15, 10]

# Create an object of TimSort
timsort_obj = TimSort()

# Perform Timsort on the list
sorted_nums = timsort_obj.timSort(nums)

print("Sorted list:", sorted_nums)
