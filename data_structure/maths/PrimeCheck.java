public class PrimeCheck {
    public static void main(String[] args) {
        int n = 2; // Example number
        boolean isPrime = primeCheck(n);
        System.out.println(n + " is prime: " + isPrime + " " + 12 % 6);
        System.out.println("Count of primes less than " + n + ": " + primeCount(n));
    }

    public static boolean primeCheck(int n){
        for(int i = 2; i <Math.sqrt(n); i++){
            if(n % i == 0) return false;
        }
        return true;
    }

        // https://leetcode.com/problems/count-primes/
    public static int primeCount(int n){
        int count = 0;
        if(n <=1) return 0;
        boolean[] arr = new boolean[n+1];//consider by default all the false are prime
        arr[0] = true;
        arr[1] = true; // 0 and 1 are not prime

        for(int i = 2; i*i <=n; i++){
            if(!arr[i]){
                for(int j = i*2; j<=n; j+=i){
                    arr[j] = true; // mark multiples of i as not prime
                }
            }
        }

        for(int i = 0; i < arr.length; i++){
            if(!arr[i]) count++;
        }
        return count;
    }
}
