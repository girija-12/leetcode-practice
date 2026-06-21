class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        print(costs)
        i=0
        count=0
        for x in range(len(costs)):
            i+=costs[x]
            if i>coins:
                break
            count+=1
        return count