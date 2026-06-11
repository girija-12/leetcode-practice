class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        return (map(sum, zip(accumulate(nums), accumulate(accumulate(nums, max)))))