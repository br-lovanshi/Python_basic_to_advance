public class DigitSum {
    public static void main(String[] args) {
        int n = 12345;
        System.out.println("Sum of digits in " + n + " is: " + sumOfDigits(n));
    }

    // Function to calculate the sum of digits of a number
    public static int sumOfDigits(int n) {
        if(n == 0){
            return n;
        }
        return n % 10 + sumOfDigits(n/10);
    }
    

    public static int factorial(int n ){
        if(n == 0 || n == 1){
            return 1;
        }
        return n * factorial(n - 1);
    }
}
