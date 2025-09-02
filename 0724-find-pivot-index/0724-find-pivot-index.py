class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum=0
        total=sum(nums)
        for i in range(len(nums)):
            rightSum = total - leftSum - nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1