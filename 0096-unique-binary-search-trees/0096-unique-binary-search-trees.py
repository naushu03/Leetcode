class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def fact(n):
            if n==0 or n==1:
                return n
            else:
                return n*fact(n-1)
        return fact(2*n)//(fact(n)*fact(n+1))
        