class Solution {
    public boolean hasDuplicate(int[] nums) {
        if (nums == null || nums.length <= 1) {
            return false;
        }
        
        Set<Integer> encountered = new HashSet<>();

        for(int i = 0; i < nums.length; i++) {
            int currVal = nums[i];

            if (encountered.contains(currVal)) {
                return true;
            } else {
                encountered.add(currVal);
            }
        }

        return false;
    }
}