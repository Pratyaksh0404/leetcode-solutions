class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        o1 = (need1*cost1) + (need2*cost2)
        k2 = min(need1,need2)
        o2 = (k2*costBoth) + ((need1-k2)*cost1) + ((need2-k2)*cost2)
        k3 = max(need1,need2)
        o3 = (k3*costBoth)
        return min(o1,o2,o3)