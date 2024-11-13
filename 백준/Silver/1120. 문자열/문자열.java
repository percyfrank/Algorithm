import java.io.*;
import java.util.*;

public class Main {
    
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        String a = st.nextToken();
        String b = st.nextToken();
        
        int ans = b.length();
        for(int i=0; i<b.length()-a.length()+1; i++) {
            String target = b.substring(i,i+a.length());
            int cnt = 0;
            for(int j=0; j<a.length(); j++) {
                if(a.charAt(j) != target.charAt(j)) {
                    cnt += 1;
                }
            }
            ans = Math.min(ans, cnt);                
        }
        System.out.println(ans);
    }
}