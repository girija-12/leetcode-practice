class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x, size=0, len(nums)
        for i in range(size):
            if nums[i]!=0 and x<size:
                nums[i],nums[x]=nums[x],nums[i]
                x+=1
            