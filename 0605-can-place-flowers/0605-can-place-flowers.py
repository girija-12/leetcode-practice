class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c,size = 0, len(flowerbed)
        for i in range(0,size):
            if (flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0)) and (i==size-1 or flowerbed[i+1]==0):
                flowerbed[i]=1
                c+=1
        return c>=n