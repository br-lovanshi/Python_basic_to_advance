import java.util.Arrays;

public class FirstMissingPositive {
     public int firstMissingPositive(int[] nums) {
        int n = nums.length;
        int i = 0;
        while(i < n){
            int correctIndex = nums[i]-1;
            if(nums[i] > 0 && nums[i] < n && nums[i] != nums[correctIndex]){
                int temp = nums[i];
                nums[i] = nums[correctIndex];
                nums[correctIndex] = temp;
            }else i++;
        }

        System.out.println(Arrays.toString(nums));
        for(int num = 0; num < n; num++){
            if(nums[num] != num + 1) return num + 1;
        }

        return n+1;
    }
}

//https://leetcode.com/problems/first-missing-positive/?source=submission-noac