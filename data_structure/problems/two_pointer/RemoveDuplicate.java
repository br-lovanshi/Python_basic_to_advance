package data_structure.problems.two_pointer;

import java.util.Arrays;

public class RemoveDuplicate {
    public static void main(String[] args) {
         int[] nums = {-14,1,2,4,13,13,15,15,16,16}; // 4,1,2,3,5
         int k = removeDuplicate( nums);
         for(int i = 0; i<=k; i++){
            System.out.print(nums[i]);
         }
    }

    public static int removeDuplicate(int[] nums){
        int index = 0;
        for(int i = 1; i<nums.length; i++){
            if(nums[index] != nums[i]){
                nums[++index] = nums[i];
            }
        }
        System.out.println(Arrays.toString(nums));
        return index;
        
    }
}
// https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/