public class ReverseDigitOfNumber {
    public static void main(String[] args) {
        int n = 123;
        int reversedNumber = reverseNumber(n);
        System.out.println("Reversed number is: " + reversedNumber);
    }
    public static int reverseNumber(int n) {
        int reversed = 0;
        while (n > 0) {
            int digit = n % 10; // Get the last digit
            reversed = reversed * 10 + digit; // Append it to the reversed number
            n /= 10; // Remove the last digit from n
        }
        return reversed;
    }
}

// https://takeuforward.org/maths/reverse-digits-of-a-number
// https://leetcode.com/problems/reverse-integer/submissions/1627746929/