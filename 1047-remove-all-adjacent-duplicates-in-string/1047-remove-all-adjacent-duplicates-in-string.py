class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk=[]
        for i in s:
            if stk and stk[-1]==i:
                stk.pop()
                continue
            stk.append(i)
        return ''.join(stk)