class Solution:
    def judgeCircle(self, moves: str) -> bool:
        initial = [0,0]
        for move in moves:
            if move == "U":
                initial[1] += 1
            elif move == "D":
                initial[1] -= 1
            elif move == "L":
                initial[0] -= 1
            else:
                initial[0] += 1
        if initial == [0,0]:
            return True
        return False