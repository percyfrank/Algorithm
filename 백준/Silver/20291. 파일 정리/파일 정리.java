import java.io.*;
import java.util.*;
import java.util.Map.Entry;

public class Main {
    
    static StringBuilder sb;
    
    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Map<String,Integer> exts = new TreeMap<>();        
        for (int i=0; i<n; i++) {
            String file = br.readLine();
            String ext = file.substring(file.indexOf('.')+1);
            exts.put(ext, exts.getOrDefault(ext,0) + 1);
        }
        
        sb = new StringBuilder();
        for(Entry<String,Integer> elem : exts.entrySet()) {
            sb.append(elem.getKey()).append(" ").append(elem.getValue()).append("\n");
        }
        System.out.println(sb.toString());

    }
}