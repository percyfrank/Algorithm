import java.io.*;
import java.util.*;

public class Main {
    
    static StringTokenizer st;
    static int n, m;
    static List<Integer>[] relation;
    static boolean[] visited;
    static boolean check = false;
    
    public static void main(String[] args) throws IOException {
       
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        relation = new ArrayList[n];
        visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            relation[i] = new ArrayList<>();
        }
        
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            relation[a].add(b);
            relation[b].add(a);
        }
        
        for (int i = 0; i < n; i++) {
            visited[i] = true;
            dfs(i,1);
            visited[i] = false;
        }
        System.out.println(0);                
    }
    
    public static void dfs(int start, int depth) {
        
        if(depth == 5) {
            System.out.println(1);
            System.exit(0);
        }
        
        for(int i = 0; i < relation[start].size(); i++) {
            int next = relation[start].get(i);
            if(!visited[next]) {
                visited[next] = true;
                dfs(next,depth + 1);
                visited[next] = false;
            }
        }        
    }
}