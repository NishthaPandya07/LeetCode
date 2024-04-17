class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        def next(curr, openP, closeP):
            if openP == closeP == n:
                out.append(curr)
                return
            if openP < n:
                next(curr + '(', openP + 1, closeP )
            if closeP < openP:
                next(curr + ')', openP, closeP + 1)
        next("", 0, 0)
        return out