package data_structure.problems.sliding_window;

public class LongestSumOfSizeK {
    public static void main(String[] args) {
        int[] arr = {5,2,1,5,9,3,1,9,4};
        int k = 3;
        System.out.println(slidingWindow(arr, k));
    }

    public static int slidingWindow(int[] arr, int k){
        int maxSum = 0,  sum = 0;

        for(int i = 0; i<k; i++){
            sum += arr[i];
        }
        maxSum = sum;

        for(int i = k; i<arr.length; i++){
            sum += arr[i];
            sum -= arr[i-k];
            maxSum = Math.max(maxSum, sum);
        }

        return maxSum;
    }
}
