class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        mat = [[0] * n for _ in range(n)]

        l,r = 0,n-1
        t,b = 0,n-1

        k = 1

        while l <= r and t <= b:

            # left -> right
            for col in range(l, r + 1):
                mat[t][col] = k
                k += 1
            t += 1

            # top -> bottom
            for row in range(t, b + 1):
                mat[row][r] = k
                k += 1
            r -= 1

            # right -> left
            for col in range(r, l - 1, -1):
                mat[b][col] = k
                k += 1
            b -= 1

            # bottom -> top
            for row in range(b, t - 1, -1):
                mat[row][l] = k
                k += 1
            l += 1

        return mat