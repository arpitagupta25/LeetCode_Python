class Solution(object):
    def isPalindrome(self, s):
        rev=""
        s=s.lower()  #to lower case
        s=re.sub(r'[^a-zA-Z0-9]', '', s) #to remove non-alphanumeric character
        for i in range(len(s)-1,-1,-1):
            rev+=s[i]
        if rev==s:
            return True
        else:
            return False
        
