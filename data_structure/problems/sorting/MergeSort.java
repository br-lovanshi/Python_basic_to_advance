import java.util.Arrays;

public class MergeSort {
    public static void main(String[] args) {

        int[] nums = {64, 34, 25, 12, 22, 11, 90};
        inplaceSort(nums, 0, nums.length-1);
        System.out.println(Arrays.toString(nums));
    }

    // merge sort inplace
    public static void inplaceSort(int[] nums, int start,int end){
        if(start >= end)return;
        
        int mid = start + (end - start)/2;

        inplaceSort(nums, start, mid);
        inplaceSort(nums, mid+1, end);
        inplaceMerge(nums, start,mid,  end);

    }

    public static void inplaceMerge(int[] nums, int start, int mid, int end){
        int i = start;
        int j = mid+1;
        int k = 0;
        int[] temp = new int[end-start+1];
        while(i <= mid && j<= end){
            if(nums[i] < nums[j])
                temp[k++] = nums[i++];
            else
                temp[k++] = nums[j++];
        }
        while(i<= mid){
            temp[k++] = nums[i++];
        }
        while(j <= end){
            temp[k++] = nums[j++];
        }

        for(int p = 0; p<temp.length; p++){
            nums[start+p] = temp[p];
        }
        
    }

    public static int[] sort(int[] nums){

        if(nums.length ==1)return nums;

        int mid = nums.length/2;
        int[] left = sort(Arrays.copyOfRange(nums, 0, mid));
        int[] right = sort(Arrays.copyOfRange(nums, mid, nums.length));

        return merge(left, right);
    }

    public static int[] merge(int[] start, int[] end){
        int i =0, j = 0, k = 0;
        int n = start.length, m = end.length;
        int[] ans = new int[start.length + end.length];
        while(i < n && j <m){
            if(start[i] < end[j]){
                ans[k] = start[i];
                i++;
            }else{
                ans[k] = end[j];
                j++;
            }
            k++;
        }

        while(i < n){
            ans[k] = start[i];
            i++;
        }
        while(j < m){
            ans[k] = end[j];
            j++;
        }
        return ans;
    }
}
