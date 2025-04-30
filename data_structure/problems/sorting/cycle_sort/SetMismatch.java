public class SetMismatch{
    public int[] setMismatch(int[] nums) {
        int n = nums.length;
        int i = 0;
        while(i < n){
            int correctIndex = nums[i]-1;
            if(nums[i] != nums[correctIndex]){
                int temp = nums[i];
                nums[i] = nums[correctIndex];
                nums[correctIndex] = temp;
            }else i++;
        }
        int output[] = new int[2];
        for(int num = 0; num < n; num++){
            if(nums[num] != num + 1){
                output[0] = nums[num];
                output[1] = num + 1;
            }
        }
        return output;
    }
}