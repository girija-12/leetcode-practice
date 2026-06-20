class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=len(gain)
        arr=[0,gain[0]]
        for i in range(1, n):
            arr.append(arr[i]+gain[i])
        return max(arr)
