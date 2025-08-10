class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=list(set(nums))
        n=len(k)
        nums[:n]=k
        return n
