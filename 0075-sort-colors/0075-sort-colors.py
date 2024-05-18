class Solution:
    def sortColors(self, nums: List[int]) -> None:
        r,w,b,p=0,0,0,0
        for i in range(len(nums)):
            if nums[i]==0:
                r+=1
            if nums[i]==1:
                w+=1
            if nums[i]==2:
                b+=1
        while r>0:
            nums[p]=0
            p+=1
            r-=1
        while w>0:
            nums[p]=1
            p+=1
            w-=1
        while b>0:
            nums[p]=2
            p+=1
            b-=1
        return nums