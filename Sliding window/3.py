# step 1- start with two pointer left and right loop right pointer till length
# step 2- move right pointer and add without repeating char to set and if set has the char then remove char from set until it non repeating 
# step 3- find max length between current and new substring
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res=max(res,r-l+1)
        return res
        