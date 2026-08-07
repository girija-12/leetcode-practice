class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for _ in range(10):
            prod=1
            for i in list(str(n)):
                prod*=int(i)
            if (prod%t==0):
                return n
            n+=1