class Recursion{
    public static void main(String[] args) {
        print(5);
        System.out.println();
        System.out.println("Factorial of 5 is: " + factorial(5));
    }

    static void print(int n){
        if(n == 0){
            return;
        }
        System.out.print(n + " ");
        print(n-1);
    }

    static int factorial(int n){
        if(n == 0 || n == 1){
            return 1;
        }
        return n * factorial(n-1);
    }
}