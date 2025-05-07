public class DigitCount {
    public static void main(String[] args) {
        int n = 1235;
        int count = digitCount(n);
        System.out.println("Number of digits in " + n + " is: " + count);
    }

    public static int digitCount(int n){
        int count = 0;
        while(n>0){
            n /= 10;
            count++;
        }
        return count;
    }
}
// https://takeuforward.org/data-structure/count-digits-in-a-number/