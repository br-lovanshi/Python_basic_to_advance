package data_structure.problems.two_pointer;

import java.util.Arrays;

public class SumEqualsK {
    public static void main(String[] args) {
        int[] nums = {-12,-3,1,2,4,3};
        int target = 7;
        System.out.println(Arrays.toString(twoPointer(nums, target)));
    }

    public static int[] twoPointer(int[] nums, int target){
        int left = 0;
        int right = nums.length-1;
        while(left < right){
            int sum = nums[left] + nums[right];
            if(sum == target) return new int[]{left, right};
            if(sum > target) right--;
            else left++;
        }
        return new int[]{};
    }
}
