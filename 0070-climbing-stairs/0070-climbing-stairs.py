class Solution(object):
    def climbStairs(self, n):
        lst=[-1]*(n+1)
        def fib(n):
            if n<=1:
                return 1
            if lst[n]!=-1:
                return lst[n]
            lst[n]=fib(n-1)+fib(n-2)
            return lst[n]
        return fib(n)