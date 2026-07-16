class Solution(object):
    def applyOperations(self, nums):
        n = len(nums)

        # Step 1: Apply operations
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        # Step 2: Move non-zero elements to the front
        write = 0

        for read in range(n):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

        # Fill remaining positions with zeros
        while write < n:
            nums[write] = 0
            write += 1

        return nums
        
