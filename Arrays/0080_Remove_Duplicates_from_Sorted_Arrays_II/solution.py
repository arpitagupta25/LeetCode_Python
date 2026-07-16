class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)

        L=2
        R=2
        while R<len(nums):
            if nums[R]==nums[L-2]:
                R+=1
            else:
                nums[L]=nums[R]
                L+=1
                R+=1
        return L
