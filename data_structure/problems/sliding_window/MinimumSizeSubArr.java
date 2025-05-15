package data_structure.problems.sliding_window;

public class MinimumSizeSubArr {
    public static void main(String[] args) {
        int[] nums = {2,3,1,2,4,3};
        int target = 7;
        System.out.println(dynamicSlidingWindo(nums, target));
    }

    public static long dynamicSlidingWindo(int[] nums, int target){
        int left = 0;
        long minLen = Integer.MAX_VALUE;
        int sum = 0;
        for(int right = 0; right < nums.length; right++){
            sum += nums[right];
            while(sum >= target){
                sum -= nums[left];
                minLen = Math.min(minLen, right-left+1);
                left++;
            }
        }
        return minLen == Integer.MIN_VALUE?0:minLen;
    }
}
// https://leetcode.com/problems/minimum-size-subarray-sum/description/
