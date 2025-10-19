class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        left_prd=1
        for i in range(len(nums)):
            res[i]=left_prd
            left_prd*=nums[i]
        right_prd=1
        for i in range(len(nums)-1, -1, -1):
            res[i]*=right_prd
            right_prd*=nums[i]
        return res