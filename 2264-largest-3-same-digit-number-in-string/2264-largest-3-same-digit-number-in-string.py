class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n=len(num)
        max_good="-1"
        for i in range(n-2):
            c=num[i:i+3]
            if len(set(c))==1:
                max_good=max_good if int(max_good)>int(c) else c
        return max_good if max_good!="-1" else ""