class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        c=0
        for i in costs:
            if coins>=i:
                coins-=i
                c+=1
        return c