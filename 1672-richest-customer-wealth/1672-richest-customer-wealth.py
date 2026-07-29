class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxi=0
        for i in range(len(accounts)):
            maxi=max(maxi,sum(accounts[i]))
        return maxi