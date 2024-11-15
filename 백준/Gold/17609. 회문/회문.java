import java.io.*;
import java.util.*;

public class Main {
    
    static StringBuilder sb;
    
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        sb = new StringBuilder();
        
        
        for(int i=0; i<n; i++){
            String word = br.readLine();
            sb.append(checkPalindrome(0,word.length()-1,word,0)).append("\n");
        }
        System.out.println(sb.toString());
    }
    
    public static int checkPalindrome(int start, int end, String word, int cnt) {
       
        if (cnt >= 2) {
            return 2;
        }
        
        while (start < end) {
            if(word.charAt(start) == word.charAt(end)) {
                start += 1;
                end -= 1;
            } else {
                return Math.min(checkPalindrome(start+1,end,word,cnt+1),checkPalindrome(start,end-1,word,cnt+1));
            }            
        }
        
        return cnt;
    }
}