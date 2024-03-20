class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_arr = nums1 + nums2       # merge two array
        sorted_arr= sorted(merged_arr)   # sorted merge array
        mid = len(sorted_arr)//2
        l= len(sorted_arr)
        if (l%2) ==0:
            return (sorted_arr[mid-1] + sorted_arr[mid])/2
        else:
            return sorted_arr[mid]
        