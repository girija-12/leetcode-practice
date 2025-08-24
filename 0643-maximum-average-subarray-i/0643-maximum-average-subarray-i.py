class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        wind=sum(nums[0:k])
        max_av=wind/k
        for i in range(k,n):
            wind+=nums[i]-nums[i-k]
            max_av=max(max_av,wind/k)
        return max_av