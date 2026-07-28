class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxs=heapq.nlargest(2, nums)
        return (maxs[0]-1)*(maxs[1]-1)