public class PalindromNum {
    public static void main(String[] args) {
        int n = 121;
        boolean isPalindrome = isPalindrome(n);
        if (isPalindrome) {
            System.out.println(n + " is a palindrome number.");
        } else {
            System.out.println(n + " is not a palindrome number.");
        }
    }

    public static boolean isPalindrome(int n){
        int originalNum = n;
        int reverseNum = 0;
        while(n >0){
            int digit = n % 10;
            reverseNum = reverseNum * 10 + digit;
            n /= 10;
        }
        return reverseNum == originalNum;
    }
}
