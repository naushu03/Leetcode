class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res=[]
        def solve(temp,i):
            if len(temp)==k:
                res.append(list(temp))
                return
            if i>n:
                return
            temp.append(i)
            solve(temp,i+1)
            temp.pop()
            solve(temp,i+1)
        solve([],1)
        return res