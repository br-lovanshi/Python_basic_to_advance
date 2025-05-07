import java.util.Arrays;

public class PrefixSum{
    public static void main(String[] args) {
        int n = 5;
        int[] arr = {1, 2, 3, 4, 5};
        prefixSum(arr);
        sufixSum(arr);
    }

    public static void prefixSum(int[] arr){
        int n = arr.length;
        int[] prefixSum = new int[n];
        prefixSum[0] = arr[0];
        for(int index = 1; index < n; index++){
            prefixSum[index] = prefixSum[index - 1] + arr[index];
        }

        // Print the prefix sum array
        System.out.println("Prefix Sum Array: " + Arrays.toString(prefixSum)); 
    }

    public static void sufixSum(int[] arr) {
       int n = arr.length;
       int[] suffixSum = new int[n];

       suffixSum[n - 1] = arr[n - 1];
       for(int i = n-2; i>=0; i--){
            suffixSum[i] = suffixSum[i + 1] + arr[i];
       }

       System.out.println("suffix Sum Array: " + Arrays.toString(suffixSum)); 

    }
}