class Solution:
    def minPartitions(self, n: str) -> int:
        for i in "9876543210":
            if i in n:
                return int(i)