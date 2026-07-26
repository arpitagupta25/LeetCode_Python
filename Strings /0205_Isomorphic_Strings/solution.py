class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)!=len(t):
            return False
        iso_dict={}
        for i in range(len(s)):
            if s[i] not in iso_dict:
                if t[i] not in iso_dict.values():
                    iso_dict[s[i]]=t[i]
                else:
                    return False
            else:
                if iso_dict[s[i]]==t[i]:
                    continue
                return False
        return True

        
