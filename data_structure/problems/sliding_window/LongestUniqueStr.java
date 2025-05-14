package data_structure.problems.sliding_window;

import java.util.Set;
import java.util.HashSet;;

public class LongestUniqueStr {
    public static void main(String[] args) {
        String str = "aiebbaibedi";
        System.out.println(slidingWindow(str));
    }

    // Dynamic sliding window
    public static int slidingWindow(String str){
        int left = 0, maxLen = 0;
        Set<Character> set = new HashSet<>();
        for(int right = 0; right < str.length(); right++){
            while(set.contains(str.charAt(right))){
                set.remove(str.charAt(left));
                left++;
            }
            set.add(str.charAt(right));
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}
