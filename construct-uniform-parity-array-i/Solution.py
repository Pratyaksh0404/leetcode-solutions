class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        e, o = 0, 0

        for i in nums1:
            if i % 2 == 0:
                e += 1
            else:
                o += 1

        if e == 0 or o == 0 or e >= 1 or o >= 1:
            return True

        return False