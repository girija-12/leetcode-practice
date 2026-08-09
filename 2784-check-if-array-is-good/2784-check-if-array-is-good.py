class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n=len(nums)
        base=[x for x in range(1,n)]+[n-1]
        return base==sorted(nums)
