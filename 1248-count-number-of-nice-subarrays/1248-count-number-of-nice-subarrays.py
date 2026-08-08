class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmost(nums,k):
            pref=0
            res=0
            left=0
            for right in range(len(nums)):
                pref+=nums[right]%2
                while pref>k:
                    pref-=nums[left]%2
                    left+=1
                res+=right-left+1
            return res
        return atmost(nums,k)-atmost(nums,k-1)