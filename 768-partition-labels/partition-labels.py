class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hm = {}
        for i in range(0,len(s)):
            if s[i] not in hm:
                hm[s[i]] = []
            elif len(hm[s[i]]) > 1:
                hm[s[i]].pop(-1)
            hm[s[i]].append(i)

        val = list(hm.values())
        for v in val:
            if len(v) != 2:
                v.append(v[0])

        # merge intervals
        lis = [val[0]]
        pre = val[0][1]
        for i in range(1,len(val)):
            if val[i][0] <= pre:
                pre = max(val[i][1],pre)
                lis[-1][1] = pre
            else:
                lis.append(val[i])
                pre = max(val[i][1],pre)

        res = []
        for l in lis:
            res.append(l[1]-l[0]+1)
    
        return res

        