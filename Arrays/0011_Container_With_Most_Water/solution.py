class Solution(object):
    def maxArea(self, height):
        n=len(height)
        left=0
        right=n-1
        maximum = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            maximum = max(maximum, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maximum
