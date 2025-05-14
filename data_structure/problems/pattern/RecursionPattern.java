package data_structure.problems.pattern;

public class RecursionPattern {
    public static void main(String[] args) {
        decreasingTriangel(4,0);
        increasingTriangel(4, 0);
    }
    
    public static void increasingTriangel(int r, int c){
        if(r<=0)return;
        if(c <=r){
            System.err.print("* ");
            increasingTriangel(r, c+1);
        }else{
            System.out.println();
            increasingTriangel(r-1, 0);
        }
    }

    public static void decreasingTriangel(int r, int c){
        if(r <= 0){
            return;
        }
       
        if(c <= r){
            System.out.print("* ");
            decreasingTriangel(r, c+1);
        }else{
            System.out.println();
            decreasingTriangel(r-1, 0);
        }

    }
}
