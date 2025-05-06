public class NegativeAndDuplicateExceptOne {
    public static void main(String[] args) {
        int [] nums = {4, 5, 2, 1, -4, -1, -5};
        int sum = -1;
        for(int num : nums){
            sum += num;
        }
        
        System.out.println("Non negative and unique number: " + sum); // Output: 2
    }
}
