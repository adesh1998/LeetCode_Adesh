class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

    # Solution 1- 
        # l=1
        # w=k+1
        # for r in range(len(nums)):
        #     if r+w<=len(nums)and nums[r] in nums[l:r+w]:
        #         return True
        #     elif r+w>len(nums) and nums[r] in nums[l:]:
        #         return True
        #     else:
        #         l+=1
        # return False

    # Solution 2- Optimized 
        if k==0:
            return False
        s=set()
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            s.add(nums[i])
            if len(s)==k+1:
                s.remove(nums[i-k])
        return False


