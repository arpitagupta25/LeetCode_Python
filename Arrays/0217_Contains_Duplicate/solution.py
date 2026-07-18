class Solution(object):
    def containsDuplicate(self, nums):
        unique_elements=list(set(nums))
        if len(unique_elements)!=len(nums):
            return True
        else:
            return False
