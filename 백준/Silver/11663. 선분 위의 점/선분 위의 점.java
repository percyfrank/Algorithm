import java.io.*;
import java.util.*;

public class Main {
    
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        int[] points = new int[n];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++) {
            points[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(points);
        
        StringBuffer sb = new StringBuffer();
        for(int i=0; i<m; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            sb.append(upperBound(points,end)-lowerBound(points,start)).append("\n");
        }
        System.out.println(sb.toString());
    }
    
    public static int lowerBound(int[] arr, int key) {
        
        int lo = 0;
        int hi = arr.length;
        
        while (lo < hi) {
            int mid = (lo + hi) / 2;            
            if (key <= arr[mid]) {
                hi = mid;                
            } else {
                lo = mid + 1;                
            }            
        }
        return lo;
    }
    
    public static int upperBound(int[] arr, int key) {
        
        int lo = 0;
        int hi = arr.length;
        
        while (lo < hi) {
            int mid = (lo + hi) / 2;            
            if (key < arr[mid]) {
                hi = mid;                
            } else {
                lo = mid + 1;                
            }            
        }
        return lo;
    }
}