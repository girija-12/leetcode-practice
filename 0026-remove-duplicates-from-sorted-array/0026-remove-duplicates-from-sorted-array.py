class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=set(nums)
        res=[]
        for x in nums:
            if x in k:
                res.append(x)
                k.discard(x)
        n=len(res)
        nums[:n]=res
        return n
