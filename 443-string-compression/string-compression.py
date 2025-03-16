class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n==1:
            return 1
        prechar = chars[0]
        count = 1
        i = 1
        curr = n
        while i<=n:
            if i < n and chars[i] == prechar:
                count += 1
            else:
                chars.insert(curr,prechar)
                curr += 1
                if count > 1:
                    temp = str(count)
                    for c in temp:
                        chars.insert(curr,c)
                        curr+=1
                count = 1
                prechar = chars[i]
            i += 1
        
        val = curr-n
        for i in range(val):
            chars[i] = chars[n+i]
        return val