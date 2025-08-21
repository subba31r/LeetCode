class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = {0,0};
        Map<Integer, Integer> hm = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            int val = target-nums[i];
            if(hm.containsKey(val)){
                res[0] = hm.get(val);
                res[1] = i;
                return res;
            }
            hm.put(nums[i],i);
        }
        return res;
    }
}