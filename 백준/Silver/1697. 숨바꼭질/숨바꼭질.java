import java.io.*;
import java.util.*;

public class Main {

    static StringTokenizer st;
    static int n,k;
    static int[] dp = new int[100001];

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());        
        
        for (int i = 0; i <= k; i++) {
            if (i <= n) {
                dp[i] = n - i;
            } else {
                dp[i] = dp[i-1] + 1;
                if (i % 2 == 0) {
                    dp[i] = Math.min(dp[i],dp[i/2] + 1);
                } else {
                    dp[i] = Math.min(dp[i],dp[(i+1)/2] + 2);
                }
            }                
        }
        System.out.println(dp[k]);
    }
}