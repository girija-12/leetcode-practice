class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        i=0
        count=0
        for x in costs:
            i+=x
            if i>coins:
                break
            count+=1
        return count