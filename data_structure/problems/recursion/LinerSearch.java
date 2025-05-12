import java.util.ArrayList;

public class LinerSearch {
    public static void main(String[] args) {
        int[] arr = {1, 2, 2, 3, 4, 5};
        linearSearch(arr, 3, 0);
        System.out.println(isSorted(arr, 1));
        System.out.println(getList(arr,new ArrayList<>(),0,2));
        
    }

    public static int linearSearch(int[] arr, int target, int index) {
        if(index >= arr.length) return -1;
        if(arr[index] == target) return index;
        else return linearSearch(arr, target, index+1);
    }

    public static boolean isSorted(int[] arr, int index){
       
        if(index == arr.length-1) return true;

        return arr[index-1] <= arr[index] && isSorted(arr, index+1);
    }

    // return list of duplicate
    public static ArrayList<Integer> getList(int[] arr, ArrayList<Integer> list, int index, int target){
        if(index == arr.length-1)return list;
        if(arr[index] == target) list.add(index);
        return getList(arr, list, index+1, target);
    }
}