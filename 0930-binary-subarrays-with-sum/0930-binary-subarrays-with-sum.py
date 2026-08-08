class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(nums,k):
            if k<0:
                return 0
            pref=0
            res=0
            left=0
            for right in range(len(nums)):
                pref+=nums[right]
                while pref>k:
                    pref-=nums[left]
                    left+=1
                res+=right-left+1
            return res
        return atmost(nums,goal)-atmost(nums,goal-1)