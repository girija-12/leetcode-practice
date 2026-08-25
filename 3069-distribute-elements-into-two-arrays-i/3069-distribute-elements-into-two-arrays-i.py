class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l1=nums[0]
        arr1=[l1]
        arr2=[nums[1]]
        for i in range(2, n):
            if arr1[-1]>arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1+arr2
        