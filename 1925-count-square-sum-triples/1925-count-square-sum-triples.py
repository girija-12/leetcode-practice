import math
class Solution:
    def countTriples(self, n: int) -> int:
        sq_sum=0
        count=0
        for i in range(1, n+1):
            for j in range(1, n+1):
                sq_sum=i**2+j**2
                c=math.isqrt(sq_sum)
                if c*c==sq_sum and c<=n:
                    count+=1
        return count
