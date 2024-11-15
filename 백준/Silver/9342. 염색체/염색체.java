import java.io.*;
import java.util.regex.Pattern;

public class Main {
    
    static StringBuilder sb;
    
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String regex = "^[A-F]?A+F+C+[A-F]?$";
        sb = new StringBuilder();
               
        for(int i=0; i<n; i++){
            String word = br.readLine();
            if(Pattern.matches(regex,word)) {
                sb.append("Infected!").append("\n");
            } else {
                sb.append("Good").append("\n");
            }
        }

        System.out.println(sb.toString());
    }
}