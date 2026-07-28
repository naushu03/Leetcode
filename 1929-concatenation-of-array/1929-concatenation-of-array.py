class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        
        for i in range(len(nums)*2):
            ans.append(nums[i%(len(nums))])
        return ans
        