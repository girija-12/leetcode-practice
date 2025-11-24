class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count={}
        n=len(nums)
        missing=duplicate=-1
        for i in nums:
            count[i]=count.get(i,0)+1
        for i in range(1, n+1):
            if i in count:
                if count[i]==2:
                    duplicate=i
            else:
                missing=i
        return [duplicate, missing]
