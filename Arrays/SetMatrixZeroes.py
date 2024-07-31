class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows = set()
        cols = set()
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    rows.add(i)
                    cols.add(j)
        for row in rows:
            matrix[row]=[0]*m
        for col in cols:
            for i in range(n):
                matrix[i][col]=0