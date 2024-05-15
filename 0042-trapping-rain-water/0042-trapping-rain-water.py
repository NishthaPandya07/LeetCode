class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n,area=len(height),0
        l,r=0,n-1
        max_left,max_right=height[l],height[r]
        while l<r:
            if max_left>=max_right:
                r=r-1
                max_right=max(max_right,height[r])
                area+= max_right-height[r]
            else:
                l=l+1
                max_left=max(max_left,height[l])
                area+= max_left-height[l]
        return area
       
            