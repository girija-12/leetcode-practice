class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        tot=coins
        count=0
        for x in costs:
            if x<=tot:
                count+=1
                tot-=x
        return count