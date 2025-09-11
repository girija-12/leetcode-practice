class Solution:
    def removeStars(self, s: str) -> str:
        arr=[]
        for i in s:
            if (i=='*'):
                arr.pop()
                continue
            arr.append(i)
        return ''.join(arr)