public class SqareRootOfNumber {
    public static void main(String[] args) {
        int n = 16; // Example number
        double sqrt = binarySearch(n);
        System.out.println("Square root of " + n + " is: " + sqrt);
    }

   public static int binarySearch(int n){
        int start = 0;
        int end = n;
        int ans = 0;
        while(start <= end){
            int mid = start + (end - start) / 2;
            if((logn) mid * mid <= n){
                ans = mid;
                start = mid + 1;
            
            }else{
                end = mid - 1;
            }
        }
        return ans;
   }

   //https://leetcode.com/problems/sqrtx/description/
}