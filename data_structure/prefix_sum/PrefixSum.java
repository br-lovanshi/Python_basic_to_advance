import java.util.Arrays;

public class PrefixSum{
    public static void main(String[] args) {
        int n = 5;
        int[] arr = {1, 2, 3, 4, 5};
        int[] prefixSum = new int[n];
        prefixSum[0] = arr[0];
        for(int index = 1; index < n; index++){
            prefixSum[index] = prefixSum[index - 1] + arr[index];
        }

        // Print the prefix sum array
        System.out.println("Prefix Sum Array: " + Arrays.toString(prefixSum)); 
    }
}