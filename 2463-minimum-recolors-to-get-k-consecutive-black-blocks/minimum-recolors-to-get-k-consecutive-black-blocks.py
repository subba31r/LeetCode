class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        wb = 0
        bb = 0
        res = float('inf')
        i = 0
        count = 0
        while i < len(blocks):
            if count == k:
                res = min(res,wb)
                if blocks[i-k] == 'W':
                    wb -= 1
                elif blocks[i-k] == 'B':
                    bb -= 1
                count -= 1
            if blocks[i] == 'W':
                wb += 1
            elif blocks[i] == 'B':
                bb += 1
            i+=1
            count += 1
        res = min(res,wb)
        return res