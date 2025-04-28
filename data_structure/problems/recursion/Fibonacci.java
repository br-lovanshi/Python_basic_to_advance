public class Fibonacci{
    public static void main(String[] args) {
        int n = 3;
        System.out.println("Fibonacci of " + n + " is: " + fibonacci(n));
    }

    static int fibonacci(int n){
        if(n < 2){
            return n;
        }
        return fibonacci(n-1) + fibonacci(n-2);
        
    }
}