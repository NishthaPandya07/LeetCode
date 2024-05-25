class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        def backtrack(candidates, currNbr, comb):   # Extra parameter
            if currNbr == 0:
                ans.append(comb.copy())
                return
            elif currNbr < 0:
                return
            for nbr in reversed(candidates):  #  Reversed iteration 
                comb.append(nbr)
                backtrack(candidates[:], currNbr - nbr, comb)  # Pass a copy
                comb.pop()
                candidates.pop()  # The discarded element should not be used 
        backtrack(candidates, target, comb = [])  #  Extra argument
        return ans
                    