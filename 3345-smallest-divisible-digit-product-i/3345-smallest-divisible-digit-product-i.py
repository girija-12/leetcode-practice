class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for _ in range(10):
            temp=n
            prod=1
            while(temp>0):
                prod*=(temp%10)
                temp//=10
            if (prod%t==0):
                return n
            n+=1