class Solution(object):
    def isValid(self, s):
        stk=[]
        pair={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for i in s:
            if i in ["(","[","{"]:
                stk.append(i)
            elif i in [")","]","}"]:
                if not stk:
                    return False
                if stk[-1]==pair[i]:
                    stk.pop()
                else:
                    return False
        return len(stk)==0


        
