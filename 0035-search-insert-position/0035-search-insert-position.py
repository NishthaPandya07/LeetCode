class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(float('inf'))
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>target:
                if mid==0:
                    return 0
                if nums[mid-1]<target:
                    return mid
                if nums[mid-1]>target and nums[l]==nums[mid-1]:
                    return 0
                r=mid-1
            elif nums[mid]<target: 
                if nums[mid+1]>target:
                    return mid+1
                l=mid+1
            else:
                return mid

                    
                
                
        