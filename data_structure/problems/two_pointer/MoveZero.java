package data_structure.problems.two_pointer;

import java.util.Arrays;
public class MoveZero {
    public static void main(String[] args) {
        int[] nums = {0,1,0,3,12};
        moveZero(nums);
        System.out.println(Arrays.toString(nums));
    }

    public static void moveZero(int[] nums){
        int index = 0;
        for(int num = 0; num<nums.length; num++){
            if(nums[num] != 0){
                // swap
                int temp = nums[index];
                nums[index] = nums[num];
                nums[num] = temp;
                index++;
            }
        }
    }
}

// https://leetcode.com/problems/move-zeroes/submissions/1216639000/
// https://leetcode.com/problems/apply-operations-to-an-array/submissions/1634323218/