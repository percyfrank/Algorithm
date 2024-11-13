import java.io.*;
import java.util.*;
import java.util.Map.Entry;

public class Main {
        
    static StringBuilder sb;
    
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        Map<Character,Integer> map = new HashMap<>();
        for(int i=0; i<n; i++) {
            String fullName = br.readLine();
            Character lastName = fullName.charAt(0);
            map.put(lastName,map.getOrDefault(lastName,0) + 1);
        }
        
        sb = new StringBuilder();
        for(Entry<Character,Integer> elem : map.entrySet()) {
            if(elem.getValue() >= 5) {
                sb.append(elem.getKey());
            }
        }
        if (sb.toString().length() == 0) {
            System.out.println("PREDAJA");
        } else {
            char[] charArr = sb.toString().toCharArray();
            Arrays.sort(charArr);
            System.out.println(new String(charArr));
        }
        
    }
}