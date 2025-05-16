class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1],[1,1]]
        if numRows <=2:
            return res[:numRows]
        while numRows > 2:
            temp = []
            for i in range(0,len(res[-1])-1):
                temp.append(res[-1][i]+res[-1][i+1])
            temp.append(1)
            temp.insert(0,1)
            res.append(temp)
            numRows-=1
        return res
