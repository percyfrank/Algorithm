import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] nums = new int[n+1];
        int[] prefix_sum = new int[n+1];
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for(int i=1; i<=n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
            prefix_sum[i] = prefix_sum[i - 1] + nums[i];
        }
        
        long sum = 0;
        for(int i=1; i<=n; i++) {
            sum += nums[i] * prefix_sum[i - 1];
        }
        
        System.out.println(sum);

    }

}