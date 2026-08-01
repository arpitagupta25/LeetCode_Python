class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        rev=0
        org=x
        while org>0:
            num=org%10
            rev=rev*10+num
            org=org//10
        if rev==x:
            return True
        else:
            return False
