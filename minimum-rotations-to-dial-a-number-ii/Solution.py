class Solution:
    def minRotations(self, n: int, s: str) -> int:
        A = [int(c) for c in s]
        D = [[min(abs(i - j), 10 - abs(i - j)) for j in range(10)] for i in range(10)]
        
        base = 0
        prev = 0
        for a in A:
            base += D[prev][a]
            prev = a
            
        last = A[-1]
        mini = 0
        
        for i in range(n):
            p = 0 if i == 0 else A[i-1]
            diff = D[p][last] - D[p][A[i]]
            if diff < mini:
                mini = diff
                
        return base + mini