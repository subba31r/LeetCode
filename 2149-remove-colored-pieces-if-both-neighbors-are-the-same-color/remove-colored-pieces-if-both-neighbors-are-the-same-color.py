class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a, b = 0, 0
        acur, bcur = 0, 0
        for c in colors:
            if c=='A':
                if bcur >=3:
                    b += bcur-2
                bcur = 0
                acur += 1
            else:
                if acur >= 3:
                    a += acur-2
                acur = 0
                bcur += 1
        if acur>=3: a += acur-2
        if bcur>=3: b += bcur-2
        return b<a
