class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        first = date.fromisoformat('2001-' + max(arriveAlice, arriveBob))
        last  = date.fromisoformat('2001-' + min(leaveAlice, leaveBob))
        
        return max((last - first).days + 1, 0)