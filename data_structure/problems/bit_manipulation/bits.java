public class bits {
    public static void main(String[] args) {
        // Example usage
        // bit operators
        int a = 5; // 0101
        int b = 3; // 0011
        System.out.println("a & b: " + (4 & 1)); // 0001
        System.out.println("a | b: " + (a | b)); // 0111
        System.out.println("a ^ b: " + (a ^ b)); // 0110
        // System.out.println("~a: " + (~a)); // 1010
        // System.out.println("a << 1: " + (a << 1)); // 1010
        // System.out.println("a >> 1: " + (a >> 1)); // 0010

        System.out.println("isEven(5): " + isEven(5)); // true
    }

    public static boolean isEven(int n){
        // Check if a number is even using bitwise AND
        return (n & 1) == 1 ? false : true;
    }
}
