class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        HashMap<Integer,Integer> map = new HashMap();
        // fill HasMap
        for(int i=0;i<nums.length;i++)
        {
            map.put(nums[i],i);
        }
        // searching
        for(int i=0;i<nums.length;i++)
        {
            int num = nums[i]; 
            int rem = target - num; // rem means remaining number
            if(map.containsKey(rem))  // check that remaining number is exist in the array
            {
                int index= map.get(rem); // give the index of remaining number
                if(i==index)
                {
                    continue;
                }
                return new int[]{i,index}; //return the array of index number for both number
            }
        }
        return new int[]{};
    }
}

// Time Complexity = O(n)
// Space Complexity = O(n)