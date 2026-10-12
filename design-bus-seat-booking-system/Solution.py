class BusBooking:

    def __init__(self, n: int):
        self.n=n
        self.cost={}
        self.total=0

    def toggle(self, seat: str) -> None:
        if seat in self.cost:
            self.total-=self.cost.pop(seat)
            return
        l,row=seat[0],seat[1:]
        c=1
        if l=='A' and ('B'+row) in self.cost:
            c=3
        elif l=='D' and ('C'+row) in self.cost:
            c=3
        self.cost[seat]=c
        self.total+=c
        
    def getTotalTime(self) -> int:
        return self.total

    def getMinTime(self) -> int:
        return len(self.cost)

