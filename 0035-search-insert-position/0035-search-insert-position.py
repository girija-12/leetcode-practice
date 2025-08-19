class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        i, n=0, len(nums)
        while(i<n and nums[i]<target):
            i+=1
        return i