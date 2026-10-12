class BusBooking:

    def __init__(self, n: int):
        self.bb = set()
        self.tt = 0
        self.cc = {}

    def toggle(self, seat: str) -> None:
        if seat in self.bb:
            self.bb.remove(seat)
            cost = self.cc.pop(seat)
            self.tt -= cost
        else:
            self.bb.add(seat)
            c,r = seat[0],seat[1:]
            adj = 'B' if c=='A' else ('C' if c=='D' else None)
            cost = 3 if adj and f"{adj}{r}" in self.bb else 1
            self.cc[seat] = cost
            self.tt += cost
            

    def getTotalTime(self) -> int:
        return self.tt

    def getMinTime(self) -> int:
        return len(self.bb)


# Your BusBooking object will be instantiated and called as such:
# obj = BusBooking(n)
# obj.toggle(seat)
# param_2 = obj.getTotalTime()
# param_3 = obj.getMinTime()