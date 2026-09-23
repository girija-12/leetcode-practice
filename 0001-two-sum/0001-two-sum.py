class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for i, val in enumerate(nums):
            rem=target-val
            if rem in seen:
                return [i, seen[rem]]
            seen[val]=i