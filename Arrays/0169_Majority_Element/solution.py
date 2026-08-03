class Solution(object):
    def majorityElement(self, nums):
        dict_cnt={}
        for i in range(len(nums)):
            if nums[i] not in dict_cnt:
                dict_cnt[nums[i]]=1
            else:
                dict_cnt[nums[i]]=dict_cnt[nums[i]]+1

            if dict_cnt[nums[i]]>len(nums)//2:
                    return nums[i]


