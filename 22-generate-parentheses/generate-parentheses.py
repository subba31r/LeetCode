class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        op,cl = 0,0
        res = []

        def generate(op,cl,cur):
            if op> n or cl>n:
                return
            if op==cl==n:
                res.append(cur)
                return
            if op >= cl:
                generate(op+1,cl,cur+"(")
            generate(op,cl+1,cur+")")
        generate(op,cl,"")
        return res
