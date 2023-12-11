import java.util.*;
import java.lang.Math;

class Solution {
    public String solution(String s) {
        
        String[] sArray = s.split(" ");
        int[] nums = Arrays.stream(sArray).mapToInt(Integer::parseInt).toArray();
        
        return String.valueOf(Arrays.stream(nums).min().getAsInt()) + " " + String.valueOf(Arrays.stream(nums).max().getAsInt());
    }
}