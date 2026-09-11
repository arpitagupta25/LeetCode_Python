class Solution(object):

    def totalNumbers(self, digits):

        """
        :type digits: List[int]
        :rtype: int
        """

        result=set()
        # Choose the last digit
        for i in range(len(digits)):

            if digits[i] % 2 == 0:       # last digit must be even

                # Choose the first digit
                for j in range(len(digits)):

                    if j == i:           # same digit/copy cannot be reused
                        continue

                    if digits[j] == 0:   # no leading zero
                        continue

                    # Choose the middle digit
                    for k in range(len(digits)):

                        if k == i or k == j:
                            continue
                        number=str(digits[j])+str(digits[k])+str(digits[i])
                        result.add(number)

        return len(result)
