# %%

from typing import List


class timSort:
    
    def insertionSort(self, nums:List[int], left: int, right: int) -> None:
        
        for i in range(left + 1, right + 1):

            key = nums[i]
            j = i - 1

            while j >= left and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1

            nums[j + 1] = key


    def mergeSort(self, nums:List[int], runIndex: int, leftEndIndex: int, rightEndIndex: int) -> None:

        leftSize = leftEndIndex - runIndex + 1
        rightSize = rightEndIndex - leftEndIndex

        leftArray = nums[runIndex : leftEndIndex + 1]
        rightArray = nums[leftEndIndex + 1 : rightEndIndex + 1]

        i, j, k = 0, 0, runIndex

        while i < leftSize and j < rightSize:

            if leftArray[i] <= rightArray[j]:
                nums[k] = leftArray[i]
                i += 1

            else:
                nums[k] = rightArray[j]
                j += 1

            k += 1

        while i < leftSize:
            nums[k] = leftArray[i]
            i += 1
            k += 1

        while j < rightSize:
            nums[k] = rightArray[j]
            j += 1
            k += 1



    def timSort(self, nums:List[int]) -> List[int]:

        runSize = 4
        n = len(nums)

        for start in range(0, n, runSize):
            end = min(start + runSize - 1, n - 1)
            self.insertionSort(nums, start, end)

        currentSize = runSize
        while currentSize < n:

            for runIndex in range(0, n, currentSize * 2):

                leftEndIndex = min(n - 1, runIndex + currentSize - 1)
                rightEndIndex = min(n - 1, runIndex + currentSize * 2 - 1)

                if leftEndIndex < rightEndIndex:
                    self.mergeSort(nums, runIndex, leftEndIndex, rightEndIndex)

            currentSize *= 2

        return nums



nums = [5, 21, 7, 23, 19, 2, 15, 10]
timsort = timSort()
sorted_nums = timsort.timSort(nums)
print(sorted_nums)





from typing import List


class Timsort:
    def insertionSort(self, nums: List[int], left: int, right: int) -> None:
        # Perform insertion sort on the sublist nums[left:right + 1]
        for i in range(left + 1, right + 1):
            key = nums[i]
            j = i - 1
            # Move elements of nums[left:right] that are greater than key
            while j >= left and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key

    def merge(self, nums: List[int], left_index: int, left_run_end: int, right_run_end: int) -> None:
        # Merge two sorted sublists nums[left_index:left_run_end + 1] and nums[left_run_end + 1:right_run_end + 1]
        left_size = left_run_end - left_index + 1
        right_size = right_run_end - left_run_end
        
        # Create temporary arrays for the left and right runs
        left_array = nums[left_index:left_run_end + 1]
        right_array = nums[left_run_end + 1:right_run_end + 1]

        # Merge the temporary arrays back into the original list
        i, j, k = 0, 0, left_index

        while i < left_size and j < right_size:
            if left_array[i] <= right_array[j]:
                nums[k] = left_array[i]
                i += 1
            else:
                nums[k] = right_array[j]
                j += 1
            k += 1

        # Copy the remaining elements of left_array, if any
        while i < left_size:
            nums[k] = left_array[i]
            i += 1
            k += 1

        # Copy the remaining elements of right_array, if any
        while j < right_size:
            nums[k] = right_array[j]
            j += 1
            k += 1

    def timSort(self, nums: List[int]) -> List[int]:
        # Define the minimum run size
        min_run_size = 32
        n = len(nums)

        # Sort individual sublists of size min_run_size using insertion sort
        for start in range(0, n, min_run_size):
            end = min(start + min_run_size - 1, n - 1)
            self.insertionSort(nums, start, end)

        # Step 2: Merge the sorted runs
        current_run_size = min_run_size  # Initialize the size of runs to merge
        while current_run_size < n:       # Continue merging until the current run size exceeds the length of the list
            
            # Iterate through the list in chunks of current_run_size * 2
            # (4, 4) (4, 4) -> (8,8) -> (16)
            for left_index in range(0, n, current_run_size * 2):  
                left_run_end = min(left_index + current_run_size - 1, n - 1)  # Determine the end index of the left run
                right_run_end = min(left_index + current_run_size * 2 - 1, n - 1)  # Determine the end index of the right run

                # Only merge if there is a valid right run by comparing the index
                # at the end, both left and right index will give the same number - which we should not merge
                if left_run_end < right_run_end:
                    self.merge(nums, left_index, left_run_end, right_run_end)  # Merge the two sorted runs

            current_run_size *= 2  # Double the size of the runs for the next iteration 

        return nums

# Example usage:
nums = [5, 21, 7, 23, 19, 2, 15, 10]
timsort = Timsort()
sorted_nums = timsort.timSort(nums)
print(sorted_nums)
