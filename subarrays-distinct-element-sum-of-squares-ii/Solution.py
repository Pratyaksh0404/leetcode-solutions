class SegmentTree:
    def __init__(self, arr: list[int], l: int, r: int):
        self.lazy = 0
        if l == r:
            self.l = self.r = l
            self.left = self.right = None
            self.sum = arr[l]
            self.squareSum = arr[l] * arr[l]
        else:
            self.l = l
            self.r = r
            mid = (r + l) // 2
            self.left = SegmentTree(arr, l, mid)
            self.right = SegmentTree(arr, mid + 1, r)
            self.sum = self.left.sum + self.right.sum
            self.squareSum = self.left.squareSum + self.right.squareSum
    
    def getSquareSum(self, l: int, r: int):
        if l <= self.l and self.r <= r:
            return self.squareSum
        elif self.l > r or self.r < l:
            return 0
        else:
            return self.left.getSquareSum(l, r) + self.right.getSquareSum(l, r)
    
    def add(self, l: int, r: int, k: int):
        if self.lazy > 0:
            selfK = self.lazy
            self.lazy = 0
            self.add(self.l, self.r, selfK)

        if l <= self.l and self.r <= r:
            self.squareSum += (2 * k * self.sum + k * k * (self.r - self.l + 1))
            self.sum += k * (self.r - self.l + 1)
            
            if self.left != None:
                self.left.lazy += k
            if self.right != None:
                self.right.lazy += k
        elif self.l > r or self.r < l:
            return
        else:
            self.left.add(l, r, k)  
            self.right.add(l, r, k)
            self.sum = self.left.sum + self.right.sum
            self.squareSum = self.left.squareSum + self.right.squareSum

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        m = 1000000007
        root = SegmentTree([0] * len(nums), 0, len(nums) - 1)
        lastSeen = {}

        for i in range(len(nums)):
            st = 0
            if nums[i] in lastSeen:
                st = lastSeen[nums[i]] + 1
            root.add(st, i, 1)
            ans = (ans + root.getSquareSum(0, len(nums) - 1)) % m
            lastSeen[nums[i]] = i

        return ans