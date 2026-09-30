class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        for row in range(numRows):
            temp = [1] * (row + 1)  
            for j in range(1, row):
                temp[j] = ans[row - 1][j - 1] + ans[row - 1][j]
            ans.append(temp)

        return ans