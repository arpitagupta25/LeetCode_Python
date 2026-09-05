class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        int_a=int(a,2)
        int_b=int(b,2)
        sum_result=int_a+int_b
        return bin(sum_result)[2:]

  
