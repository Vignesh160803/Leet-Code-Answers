class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        res = [[1],[1,1]]
        for i in range(2,numRows):
            temp = []
            temp.append(1)
            for j in range(1,i):
                temp.append(res[i-1][j-1]+res[i-1][j])
            temp.append(1)
            res.append(temp)
        return res