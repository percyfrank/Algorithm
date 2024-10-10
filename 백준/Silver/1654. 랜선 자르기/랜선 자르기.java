import java.io.*;
import java.util.*;

public class Main {
    
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int k = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        
        int[] lans = new int[k];
        long hi = 0;
        for(int i=0; i<k; i++) {
            lans[i] = Integer.parseInt(br.readLine());
            if(hi < lans[i]) {
                hi = lans[i];
            }
        }                
        
        hi++;
        long lo = 0;
        while(lo < hi) {
            long mid = (lo + hi) / 2;
            long cnt = 0;
            for(int i=0; i<k; i++) {
                cnt += lans[i] / mid;
            }
            if(cnt < n) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        
        System.out.println(lo-1);
    }
}