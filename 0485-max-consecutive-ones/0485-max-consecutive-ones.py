class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=c=0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
                maxi=max(maxi,c)
            else:
                c=0
        return maxi