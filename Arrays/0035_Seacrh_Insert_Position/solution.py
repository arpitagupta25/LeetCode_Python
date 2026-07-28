class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            i=0
            while i <= (len(nums)):
                if i==len(nums):
                    return len(nums)
                elif nums[i]>target:
                    return i 
                i+=1
                
            
        
