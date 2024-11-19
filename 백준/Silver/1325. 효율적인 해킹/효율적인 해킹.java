import java.io.*;
import java.util.*;

public class Main {
    
    static StringTokenizer st;
    static StringBuilder sb;
    static List<Integer>[] nodes;
    static int[] cnts;
    static int[] visited;
    
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        nodes = new ArrayList[n+1];
        for(int i=0; i<n+1; i++) {
            nodes[i] = new ArrayList<>();
        }
        
        for(int i=0; i<m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            nodes[b].add(a);
        }
        
        int ans = 0;
        cnts = new int[n+1];
        for(int i=0; i<n+1; i++) {
            if(!nodes[i].isEmpty()) {
                visited = new int[n+1];
                cnts[i] = bfs(i,1);
                Arrays.fill(visited,0);
                ans = Math.max(ans,cnts[i]);
            }
        }
        
        sb = new StringBuilder();
        for(int i=1; i<n+1; i++) {
            if(cnts[i] == ans) {
                sb.append(i).append("\n");
            }
        }
        
        System.out.println(sb.toString());
    }
    
    public static int bfs(int start, int cnt) {
        
        Queue<Integer> q = new LinkedList<>();
        q.offer(start);
        visited[start] = 1;
        
        while(!q.isEmpty()) {
            int tmp = q.poll();
            for(int i=0; i<nodes[tmp].size(); i++) {
                int next = nodes[tmp].get(i);
                if(visited[next] == 0) {
                    cnt += 1;
                    visited[next] = 1;                    
                    q.offer(next);
                }
            }
        }
        
        return cnt;
    }
}