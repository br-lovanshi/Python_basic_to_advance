class Recursion{
    public static void main(String[] args) {
        print(5);
        System.out.println();
        revPrint(5);
        System.out.println();
        System.out.println("Factorial of 5 is: " + factorial(5));
        System.out.println(sum(5));
        
        
    }

    static void print(int n){
        if(n == 0){
            return;
        }
        System.out.print(n + " ");
        print(n-1);
    }

    static void revPrint(int n){
        if (n == 0){
            return;
        }
        revPrint(n-1);
        System.out.print(n + " ");
    }

    static int factorial(int n){
        if(n == 0 || n == 1){
            return 1;
        }
        return n * factorial(n-1);
    }

    static int sum(int n){
        if(n == 0){
            return n;
        }
        return n + sum(n-1);

    }
}