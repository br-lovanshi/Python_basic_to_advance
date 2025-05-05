public class SingeNonDuplicate {
    public static void main(String[] args) {
        // Example usage
        int[] nums = {4, 1, 2, 1, 2};
        System.out.println("Single number: " + singleNonDuplicate(nums)); // Output: 4
    }

    public static int singleNonDuplicate(int[] nums) {
        int sum = 0;
        for(int num : nums){
            sum ^= num;
        }
        return sum;
    }
}

// https://leetcode.com/problems/single-element-in-a-sorted-array/