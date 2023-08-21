class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        minSub=len(nums)+1
        s=0
        while r<len(nums):
            s+=nums[r]
            while s>=target:
                minSub=min(minSub,r-l+1)
                s-=nums[l]
                l+=1
            r+=1
        return 0 if minSub>len(nums) else minSub

