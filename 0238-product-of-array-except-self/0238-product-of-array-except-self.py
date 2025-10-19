class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        left_prd=1
        for i in range(n):
            res[i]=left_prd
            left_prd*=nums[i]
        right_prd=1
        for i in range(n-1, -1, -1):
            res[i]*=right_prd
            right_prd*=nums[i]
        return res