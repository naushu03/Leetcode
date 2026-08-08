class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pref=0
        res=0
        d={0:1}
        for i in nums:
            pref+=i%2
            res+=d.get(pref-k,0)
            d[pref]=d.get(pref,0)+1
        return res