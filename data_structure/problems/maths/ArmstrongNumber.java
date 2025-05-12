public class ArmstrongNumber {
    
    public static void main(String[] args){
        int n = 153;
        boolean isArmstrong = isArmstrong(n);
        if(isArmstrong){
            System.out.println(n + " is an Armstrong number.");
        } else {
            System.out.println(n + " is not an Armstrong number.");
        }
    }

    public static boolean isArmstrong(int n){
        int originalNumber = n;
        int len = String.valueOf(n).length();
        int sum = 0;
        
        while(n > 0){
            int digit = n % 10;
            sum += Math.pow(digit, len);
            n /= 10;
        }
        return sum == originalNumber;
    }
}
// https://takeuforward.org/maths/check-if-a-number-is-armstrong-number-or-not/