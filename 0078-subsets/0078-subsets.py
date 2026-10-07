class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res=[]
        n=len(nums)
        def solve(temp,i):
            if i>=n:
                res.append(list(temp))
                return
            temp.append(nums[i])
            solve(temp,i+1)
            temp.pop()
            solve(temp,i+1)
        solve([],0)
        return res