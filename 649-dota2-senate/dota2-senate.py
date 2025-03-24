class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r = [i for i in range(n) if senate[i]=="R"]
        d = [i for i in range(n) if senate[i]=="D"]

        while r and d:
            e1 = r.pop(0)
            e2 = d.pop(0)
            if e1 < e2:
                r.append(n+e1)
            else:
                d.append(n+e2)
        
        return "Radiant" if r else "Dire"