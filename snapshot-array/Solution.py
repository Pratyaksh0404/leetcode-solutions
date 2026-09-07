class SnapshotArray:

    def __init__(self, length: int):
        self.sid = 0
        self.h = [[(0, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        if self.h[index][-1][0] == self.sid:
            self.h[index][-1] = (self.sid, val)
        else:
            self.h[index].append((self.sid, val))

    def snap(self) -> int:
        self.sid += 1
        return self.sid - 1

    def get(self, index: int, sid: int) -> int:
        arr = self.h[index]
        l, r = 0, len(arr) - 1
        ans = 0

        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] <= sid:
                ans = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return ans