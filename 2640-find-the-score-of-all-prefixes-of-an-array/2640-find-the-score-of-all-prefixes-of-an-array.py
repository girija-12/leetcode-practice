class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        pref_max=0
        n=len(nums)
        conver=[0]*n
        for i in range(0,n):
            pref_max=max(pref_max, nums[i])
            conver[i]=nums[i]+pref_max
        for i in range(1, n):
            conver[i]=conver[i]+conver[i-1]
        return conver
