import java.io.*;
import java.util.*;

public class Main {
    
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        int[] heights = new int[n];
        long hi = 0;
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++) {
            heights[i] = Integer.parseInt(st.nextToken());
            if(hi < heights[i]) {
                hi = heights[i];
            }
        }                
        
        hi++;
        long lo = 0;
        while(lo < hi) {
            long mid = (lo + hi) / 2;
            long target = 0;
            for(int i=0; i<n; i++) {
                if(heights[i] >= mid) {
                    target += heights[i] - mid;
                }
            }
            if(target < m) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        
        System.out.println(lo-1);
    }
}