public class RotatedBinarySearch {
    public static void main(String[] args) {
        int[] arr = {5,6,7,8,1,2,4};
        int target = 8;
        System.out.println(binarySearch(arr, target, 0, arr.length-1));
    }

    public static int binarySearch(int[] arr, int target, int s, int e){

        if(s > e) return -1;

        int mid = s + (e-s)/2;
        if(arr[mid] == target) return mid;

        if(arr[s] <= arr[mid]){
            if(target >= arr[s] && target <= arr[mid]){
              return  binarySearch(arr, target, s, mid-1);
            }else{
              return  binarySearch(arr, target, mid+1 , e);
            }
        }
        if(target >= arr[mid] && target <= arr[e]){
           return binarySearch(arr, target, mid+1, e);
        }

        return binarySearch(arr, target, s, mid-1);
    }
}
