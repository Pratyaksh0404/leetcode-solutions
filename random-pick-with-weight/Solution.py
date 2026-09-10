class Solution:

    def __init__(self, w: List[int]):
        self.rr = []
        ss = 0

        for weight in w:
            ss += weight
            self.rr.append(ss)

        self.total_sum = ss

    def pickIndex(self) -> int:
        tar = random.randint(1, self.total_sum)
        l, r = 0, len(self.rr)

        while l <= r:
            mid = l + (r - l) // 2
            if tar > self.rr[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return l