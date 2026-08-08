class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref=0
        res=0
        d={0:1}
        for i in nums:
            pref+=i
            res+=d.get(pref-goal,0)
            d[pref]=d.get(pref,0)+1
        return res