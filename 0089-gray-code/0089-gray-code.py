class Solution:
    def grayCode(self, n: int) -> List[int]:
        res=[]
        for i in range(1<<n):
            gray=i^(i>>1)
            res.append(gray)
        return res