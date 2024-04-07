class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1: return s
        res=""
        l=len(s)
        for r in range(numRows):
            inc=2*(numRows-1)
            for i in range(r,l,inc):
                res+=s[i]
                if (0<r and r<numRows-1 and (i+inc-2*r)<l):
                    res+=s[i+inc-2*r]
        return res
                
                
                
            