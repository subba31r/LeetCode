class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = True
        #row wise
        for i in range(0,9):
            arr = [0]*10
            for j in range(0,9):
                val = board[i][j]
                if val != ".":
                    if arr[int(val)] != 0:
                        return False
                    arr[int(val)] = 1
        
        #column wise
        for i in range(0,9):
            arr = [0]*10
            for j in range(0,9):
                val = board[j][i]
                if val != ".":
                    if arr[int(val)] != 0:
                        return False
                    arr[int(val)] = 1

        #boxes
        startNum = 0
        endNum = 3
        while(startNum<9):
            arr = [0]*30
            for i in range(startNum,endNum):
                for j in range(0,9):
                    val = board[i][j]
                    if val != ".":
                        temp = int(j/3)*10 + int(val)
                        if arr[temp] != 0:
                            return False
                        arr[temp] = 1
            startNum += 3
            endNum += 3
        return res
        