class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size=len(nums)
        for i in range(size-1):
            if nums[i]==0:
                j=i+1
                while(nums[j]==0 and j<size-1):
                    j+=1
                nums[i],nums[j]=nums[j],nums[i]
            