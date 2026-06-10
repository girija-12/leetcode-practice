class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        mp={'}':'{',']':'[',')':'('}
        if len(s)%2==1:
            return False
        for i in s:
            if i in '[{(':
                stk.append(i)
            elif not stk or stk[-1]!=mp[i]:
                return False
            else:
                stk.pop()
        return not stk
                    