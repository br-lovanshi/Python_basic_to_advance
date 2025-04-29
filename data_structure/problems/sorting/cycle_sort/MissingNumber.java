public class MissingNumber {
    public int missingNumber(int[] nums) {
        int n = nums.length, i = 0;
        while(i < n){
            int correctIndex = nums[i];
            if(nums[i] < n && nums[i] != nums[correctIndex]){
                int temp = nums[i];
                nums[i] = nums[correctIndex];
                nums[correctIndex] = temp;
            }else i++;
        }
        for(int num = 0; num<n; num++){
            if(num != nums[num]){
                return num;
            }
        }

        return n;
    }
}
