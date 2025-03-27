class Solution {
    public int minimumIndex(List<Integer> nums) {
        Map<Integer,Integer> hm1 =new HashMap<>();
        Map<Integer,Integer> hm2 = new HashMap<>();
        int n = nums.size();
        for (int num : nums){
            hm2.put(num,hm2.getOrDefault(num,0)+1);
        }

        for (int i=0; i<n; i++){
            int num = nums.get(i);
            hm2.put(num,hm2.getOrDefault(num,0)-1);
            hm1.put(num,hm1.getOrDefault(num,0)+1);

            if (hm1.get(num)*2 > i+1 && hm2.get(num)*2 > n-i-1){
                return i;
            }
        }
        return -1;
    }
}