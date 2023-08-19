from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # k=len(s1)
        # l=0
        # r=k-1
        
        # while r<len(s2):
        #     cntr=Counter(s2[l:r+1])
        #     count=0
            
        #     for s in s1:
                
        #         if s in s2[l:r+1] and cntr[s]!=0:
        #             print(cntr)
        #             count+=1
        #             cntr[s]-=1
        #     print(count)
            
                
                    
        #     if count==k:
        #         print(s2[l:r+1])
        #         return True
                    
        #     l+=1
        #     r+=1
        # return False
        cnt_s1,w,match=Counter(s1),len(s1),0
        for i in range(len(s2)):
            if s2[i] in cnt_s1:
                cnt_s1[s2[i]]-=1
                if cnt_s1[s2[i]]==0:
                    match+=1
            if i>=w and s2[i-w] in cnt_s1:
                if cnt_s1[s2[i-w]]==0:
                    match-=1
                cnt_s1[s2[i-w]]+=1
            if match==len(cnt_s1):
                return True
        return False

       