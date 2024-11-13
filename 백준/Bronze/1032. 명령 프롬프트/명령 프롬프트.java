import java.io.*;
import java.util.*;

public class Main {
    
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] files = new String[n];
        for(int i=0; i<n; i++) {
            files[i] = br.readLine();
        }
        
        String answer = "";
        for(int i=0; i<files[0].length(); i++) {
            Character target = files[0].charAt(i);
            int cnt = 0;
            for(int j=0; j<n; j++) {
                if(target == files[j].charAt(i)) {
                    cnt += 1;
                }
            }
            if (cnt == n) answer += target;
            else answer += '?';            
        }
        System.out.println(answer);
    }
}