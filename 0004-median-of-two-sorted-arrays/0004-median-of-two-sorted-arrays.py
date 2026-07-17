class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n=len(nums1), len(nums2)
        nums=[]
        i, j=0,0
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                nums.append(nums1[i])
                i+=1
            else:
                nums.append(nums2[j])
                j+=1
        if i==m:
            nums.extend(nums2[j:])
        if j==n:
            nums.extend(nums1[i:])
        mid=(m+n)//2
        print(nums, mid)
        if (m+n)%2==1:
            return nums[mid]
        return (nums[mid]+nums[mid-1])/2