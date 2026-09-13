class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        return [[grid[(i+colShift[j])%n][(j+rowShift[(i+colShift[j])%n])%n] for j in range(n)] for i in range(n)]