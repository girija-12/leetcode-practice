class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            try:
                diff_ind = nums.index(diff, i + 1)
                return [i,diff_ind]
            except ValueError:
                continue