import java.io.*;
import java.util.*;
import java.util.Map.Entry;

public class Main {
    
    static StringBuilder sb;
    static StringTokenizer st;
    
    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        Map<String,Integer> names = new HashMap<>();
        
        for (int i=0; i<n; i++) {
            String name = br.readLine();
            names.put(name, names.getOrDefault(name,0) + 1);
        }
        
        for (int i=0; i<m; i++) {
            String name = br.readLine();
            names.put(name, names.getOrDefault(name,0) - 1);
        }
        
        List<String> ans = new ArrayList<>();
        for(Entry<String,Integer> elem : names.entrySet()) {
            if (elem.getValue() == 0) {
                ans.add(elem.getKey());
            }
        }
        
        sb = new StringBuilder();
        sb.append(ans.size()).append("\n");
        Collections.sort(ans);
        for(String word : ans) {
            sb.append(word).append("\n");
        }
        
        System.out.println(sb.toString());

    }
}