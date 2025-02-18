class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0 or denominator == "0":
            return "0"
        res = []
        #if only one is negativee
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
        
        n = abs(numerator)
        d = abs(denominator)
        r = n%d #remainder
        res.append(str(n//d)) #adding value before the decimal

        if r == 0:
            return "".join(res)
        res.append(".")
        rem = {}
        while r != 0 and r not in rem:
            rem[r] = len(res) #storing index in the map, so that if there is any repetition
            #we can insert ()
            r = r*10
            res.append(str(r//d))
            r = r%d

        if r in rem:
            res.insert(rem[r],"(")
            res.append(")")
        return "".join(res)

