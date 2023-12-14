import java.util.*;

class Solution {
    
    public int countNumOne(String n) {
        
        int cnt = 0;
        for(int i=0 ; i<n.length(); i++) {
            if (n.charAt(i) == '1') {
                cnt += 1;
            }
        }
        return cnt;
    }

    public int solution(int n) {
        int answer = 0;

        int targetCnt = countNumOne(Integer.toBinaryString(n));
        
        while (true) {
            n += 1;
            int cnt = countNumOne(Integer.toBinaryString(n));
            if (cnt == targetCnt) {
                return n;
            }
        }
    
    }
}