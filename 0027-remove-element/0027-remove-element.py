class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c, n=0, len(nums)
        while(val in nums):
            c+=1
            nums.remove(val)
        return n-c