public class CountZero {
    public static void main(String[] args) {
        int n = 14;
        System.out.println("Count of zeros in " + n + " is: " + countZero(n));
        System.out.println("Number of steps to reduce " + n + " to zero is: " + reduceToZero(n));
    }

    public static int reduceToZero(int n){
        if(n == 0){
            return 0;
        }
        if(n % 2 == 0){
            return 1 + reduceToZero(n / 2);
        }
        return 1 + reduceToZero(n - 1);
        
    }

    public static int countZero(int n){
        if(n == 0){
            return 1;
        }
        if(n < 10){
            return 0;
        }
        int digit = n % 10;
        if(digit == 0){
            return 1 + countZero(n / 10);
        } else {
            return countZero(n / 10);
        }
    }
}
//https://www.geeksforgeeks.org/find-number-zeroes/
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/submissions/797193328/