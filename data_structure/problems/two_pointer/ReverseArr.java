package data_structure.problems.two_pointer;

import java.util.Arrays;

public class ReverseArr {
    public static void main(String[] args) {
        
        int[] nums = {-12,-3,1,2,4,3};
        reverse(nums);
        System.out.println(Arrays.toString(nums));
    }


    public static void reverse(int[] nums){
        int start = 0, end = nums.length-1;
        while(start<end){
            int temp = nums[end];
            nums[end] = nums[start];
            nums[start] = temp;
            start++;
            end--;
        }
}
}