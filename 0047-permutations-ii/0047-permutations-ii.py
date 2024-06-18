class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]        
        lst = [] 
        u=[]
        for j in range(len(nums)):
            if nums[j] in u:    continue
            else:   u.append(nums[j])
            k = nums[j]        
            p = nums[:j] + nums[j+1:]
            for i in self.permuteUnique(p):
                lst.append([k] + i)                
        return lst