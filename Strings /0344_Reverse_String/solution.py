class Solution(object):
    def reverseString(self, s):
        n=len(s)
        for i in range(n//2):
            temp=s[i]
            s[i]=s[n-1]
            s[n-1]=temp
            n-=1
        return s 
        
