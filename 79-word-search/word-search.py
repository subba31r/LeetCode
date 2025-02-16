class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        
        row=len(board)
        col=len(board[0])

        def backtrack(r,c,ind):
            if len(word)==ind:
                return True

            if r<0 or r>=row or c<0 or c>=col or board[r][c]!=word[ind]:
                return False
            
            visited = board[r][c]
            board[r][c]="#"

            got = backtrack(r+1,c,ind+1) or backtrack(r-1,c,ind+1)or backtrack(r,c+1,ind+1) or backtrack(r,c-1,ind+1) 
            board[r][c]=visited
            return got

        for i  in range(row):
            for j in range(col):
                if backtrack(i,j,0):
                    return True
        return False



            