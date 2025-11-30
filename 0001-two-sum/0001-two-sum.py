class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            try:
                ind = nums.index(diff, i + 1)
                return [i,ind]
            except ValueError:
                continue