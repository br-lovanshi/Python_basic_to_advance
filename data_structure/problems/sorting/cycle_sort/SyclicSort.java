import java.util.Arrays;

public class SyclicSort{
    public static void main(String[] args) {
        int[] nums = {4,3,2,1,6,2};
        sort(nums);
        for(int i = 0; i<nums.length; i++){
            if(nums[i] != i + 1){
                System.out.print(i+1 + " ");
                return;
            }
        }

        System.out.println(Arrays.toString(nums));
    }

    public static void sort(int[] nums){
        int n = nums.length;

        int i = 0;
        while(i <n){
            int correctIndex = nums[i] -1;
            if(nums[i] != nums[correctIndex]){
                swap(nums, i, correctIndex);
            }else{
                i++;
            }
        }
    }

    public static void swap(int[] nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}