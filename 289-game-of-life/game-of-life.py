class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        ones = set()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 1:
                    ones.add((r,c))

        directions = [(1,0),(-1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
        for r in range(rows):
            for c in range(cols):
                count = 0
                for dr,dc in directions:
                    row = r+dr
                    col = c+dc
                    if row>=0 and row<rows and col>=0 and col<cols and (row,col) in ones:
                        count += 1
                if board[r][c] == 1:
                    if count < 2 or count>3:
                        board[r][c] = 0
                else:
                    if count == 3:
                        board[r][c] = 1
            
                    
