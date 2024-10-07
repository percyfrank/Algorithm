import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        String[] name = new String[n];
        int[] score = new int[n];
        for(int i=0; i<n; i++) {            
            st = new StringTokenizer(br.readLine());
            name[i] = st.nextToken();
            score[i] = Integer.parseInt(st.nextToken());
        }
        
        StringBuffer sb = new StringBuffer();
        for(int i=0; i<m; i++) {
            int point = Integer.parseInt(br.readLine());
            int idx = lowerBound(score, point);
            sb.append(name[idx]).append("\n");
        }
        System.out.println(sb.toString());
    }
    
    public static int lowerBound(int[] name, int key) {

        int lo = 0;
        int hi = name.length;
        
        while(lo < hi) {
            int mid = (lo+hi) / 2;
            if (key <= name[mid]) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        
        return lo;
    }
}