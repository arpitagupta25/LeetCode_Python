class Solution(object):
    def removeElement(self, nums, val):
        k=0
        i=0
        if not nums:
            return 0
        else:
            while i<len(nums):
                if nums[i]==val:
                    i+=1                    
                else:
                    nums[k]=nums[i]
                    i+=1
                    k+=1
        return k
        
