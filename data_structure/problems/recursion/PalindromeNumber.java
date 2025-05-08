public class PalindromeNumber {
    public static void main(String[] args) {
        int n = 1231;
        System.out.println("Is " + n + " a palindrome? " + isPalindrome(n));
    }

    public static boolean isPalindrome(int n) {
        // A negative number is not a palindrome
        if (n < 0) {
            return false;
        }
        // Reverse the number and check if it is equal to the original number
        return n == reverseNumber(n);
    }
    public static int reverseNumber(int n) {
        // Helper function to reverse the number
        return reverseHelper(n, 0);
    }
    private static int reverseHelper(int n, int output) {
        // Base case: if n is 0, return the output
        if (n == 0) {
            return output;
        }
        // Get the last digit and append it to the output
        int digit = n % 10;
        return reverseHelper(n / 10, output * 10 + digit);
    }
}
