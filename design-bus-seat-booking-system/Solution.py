class BusBooking:

    def __init__(self, n: int):
        self.booked = set()
        self.total_time = 0
        self.costs = {}

    def toggle(self, seat: str) -> None:
        if seat in self.booked:
            self.booked.remove(seat)
            self.total_time -= self.costs.pop(seat)
        else:
            self.booked.add(seat)
            c, r = seat[0], seat[1:]
            adj = 'B' if c == 'A' else ('C' if c == 'D' else None)
            cost = 3 if adj and f"{adj}{r}" in self.booked else 1
            self.costs[seat] = cost
            self.total_time += cost

    def getTotalTime(self) -> int:
        return self.total_time

    def getMinTime(self) -> int:
        return len(self.booked)