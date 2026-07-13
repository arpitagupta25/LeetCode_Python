class Solution(object):
    def removeDuplicates(self, nums):
        k=0
        i=0
        if not nums:
            return 0
        else:
            while i<len(nums):
                if i==0:
                    i+=1
                    k+=1
                elif nums[i]==nums[i-1]:
                    i+=1
                else:
                    nums[k]=nums[i]
                    i+=1
                    k+=1

        return k
