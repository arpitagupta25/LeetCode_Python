class Solution(object):
    def longestPalindrome(self, s):
        if len(s) == 1:
            return s

        longest = ""

        for center in range(len(s)):

            # Odd length palindrome
            left = center
            right = center

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(longest):
                    longest = s[left:right + 1]
                left -= 1
                right += 1

            # Even length palindrome
            left = center
            right = center + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(longest):
                    longest = s[left:right + 1]
                left -= 1
                right += 1

        return longest
