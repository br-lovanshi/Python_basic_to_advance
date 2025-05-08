public class ReverseNumber {
    public static void main(String[] args) {
        int n = 12345;
        System.out.println("Reversed number of " + n + " is: " + reverseNumber(n, 0));
    }

    public static int reverseNumber(int n, int output) {
    
        if(n == 0){
            return output;
        }
        int digit = n % 10;
        // output = output * 10 + digit;
       return reverseNumber(n / 10, output * 10 + digit);
    }
}
