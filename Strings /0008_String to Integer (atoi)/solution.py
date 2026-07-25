class Solution(object):
    def myAtoi(self, s):
        s = s.strip()

        if s == "":
            return 0

        Rpt = 0
        num = ""

        # Check sign
        if s[Rpt] in ["+", "-"]:
            num += s[Rpt]
            Rpt += 1

        # Skip leading zeros
        while Rpt < len(s) and s[Rpt] == "0":
            Rpt += 1

        # Read consecutive digits
        while Rpt < len(s) and s[Rpt].isdigit():
            num += s[Rpt]
            Rpt += 1

        # No digits found
        if num == "" or num == "+" or num == "-":
            return 0

        ans = int(num)

        # Clamp to 32-bit signed integer range
        if ans < -(2 ** 31):
            return -(2 ** 31)

        if ans > (2 ** 31) - 1:
            return (2 ** 31) - 1

        return ans
