public class EquilibriumIndex {
    public static void main(String[] args) {
        int[] arr = {7,1,1,5,4,5};
        int n = arr.length;
        int totalSum = 0;
        for (int i = 0; i < n; i++) {
            totalSum += arr[i];
        }
        int leftSum = 0;
        int equilibriumIndex = -1;
        for(int i = 0; i<n; i++){
            totalSum -= arr[i];
            if(leftSum == totalSum){
                equilibriumIndex = i;
                break;
            }
            leftSum += arr[i];
        }
        if (equilibriumIndex != -1) {
            System.out.println("Equilibrium index is: " + equilibriumIndex);
        } else {
            System.out.println("No equilibrium index found.");
        }
       
    }
}
