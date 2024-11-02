class Solution {
    public int search(int[] nums, int target) {
        int x = 0;
        int y = nums.length - 1;
        
        while (x <= y) {
            int mid = x + (y - x) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            else if (target < nums[mid]) {
                y = mid - 1;
            }
            else {
                x = mid + 1;
            }
        }
        return -1;
    }
}
