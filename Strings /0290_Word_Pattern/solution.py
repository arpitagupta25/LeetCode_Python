class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False

        result_dict = {}
        reverse_dict = {}

        for i in range(len(pattern)):

            char = pattern[i]
            word = words[i]

            # character already exists
            if char in result_dict:
                if result_dict[char] != word:
                    return False

            # word already exists
            if word in reverse_dict:
                if reverse_dict[word] != char:
                    return False

            # new mapping
            result_dict[char] = word
            reverse_dict[word] = char

        return True
