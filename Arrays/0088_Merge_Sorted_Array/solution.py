class Solution(object):
    def merge(self, nums1, m, nums2, n):

        temp = []

        if m == 0:
            nums1[:] = nums2
            return

        if n == 0:
            return

        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1

        if i < m:
            temp.extend(nums1[i:m])   # only valid elements

        if j < n:
            temp.extend(nums2[j:n])

        nums1[:] = temp
            
            
        
