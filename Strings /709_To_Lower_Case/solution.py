class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst_s=list(s)
        for i in range(len(lst_s)):
            if 65<= ord(lst_s[i]) <= 90:
                result_ord=ord(lst_s[i])+32
                lst_s[i]=chr(result_ord)
        
        return "".join(lst_s)
        
