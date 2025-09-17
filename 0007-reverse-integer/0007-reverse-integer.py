class Solution:
    def reverse(self, x: int) -> int:
        n=0
        t=abs(x)
        while t>0:
            r=t%10
            n=n*10+r
            t//=10
        if n < -2**31 or n > 2**31 - 1:
            return 0
        return n if x>0 else -n