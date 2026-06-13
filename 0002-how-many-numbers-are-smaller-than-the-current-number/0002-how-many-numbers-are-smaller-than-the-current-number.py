class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d={}
        ans=[]
        for i, x in enumerate(sorted(nums)):
            if x not in d: d[x]=i
        
        for i in nums:
            ans.append(d[i])
        return ans