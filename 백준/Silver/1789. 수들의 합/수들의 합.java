import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long s = Long.parseLong(br.readLine());
        
        long left = 0, right = s, ans = 0;
        while(left <= right) {
            long mid = (left + right) / 2;
            if(mid*(mid+1)/2 <= s) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;                
            }
        }
        
        System.out.println(ans);
    }
}