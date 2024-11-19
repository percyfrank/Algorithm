import java.io.*;
import java.util.*;

public class Main {
    
    static StringTokenizer st;
    static StringBuilder sb;
    static int[] visited;
    static List<Integer>[] nodes;
    
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        nodes = new ArrayList[n+1];
        for(int i=0; i<n+1; i++) {
            nodes[i] = new ArrayList<>();
        }
        
        for(int i=0; i<n-1; i++) {
            st = new StringTokenizer(br.readLine());            
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            nodes[a].add(b);
            nodes[b].add(a);                
        }
        
        visited = new int[n+1];
        dfs(1);
        
        sb = new StringBuilder();
        for(int i=2; i<n+1; i++) {
            sb.append(visited[i]).append("\n");
        }
        
        System.out.println(sb.toString());
    }
    
    public static void dfs(int start) {
        
        for(int i=0; i<nodes[start].size(); i++) {
            int next = nodes[start].get(i);
            if(visited[next] == 0) {
                visited[next] = start;
                dfs(next);
            }
        }
    }
}