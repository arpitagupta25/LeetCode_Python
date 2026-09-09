class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return -1
        else:
            frequency={}
            for char in s:
                if char not in frequency:
                    re=s.count(char)
                    frequency[char]=re
            for i in range(len(s)):
                if frequency[s[i]]>1:
                    continue
                elif frequency[s[i]]==1:
                    return i
            return -1
