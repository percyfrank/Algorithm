import java.io.*;
import java.util.*;

public class Main {

    static StringTokenizer st;
    static int n, ans, max_idx;
    static List<Node>[] graph;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new ArrayList[n+1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < n-1; i++) {
            st = new StringTokenizer(br.readLine());
            int parent = Integer.parseInt(st.nextToken());
            int child = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            graph[parent].add(new Node(child,cost));
            graph[child].add(new Node(parent,cost));            
        }
        
        visited = new boolean[n+1];
        dfs(1,0);
        visited = new boolean[n+1];
        dfs(max_idx,0);        
        System.out.println(ans);
    }

    public static void dfs(int node, int cost) {
        
        visited[node] = true;
        
        if(cost >= ans) {
            ans = cost;
            max_idx = node;
        }        
        
        for(int i = 0; i < graph[node].size(); i++) {
            Node next = graph[node].get(i);
            if(!visited[next.node]) {
                visited[next.node] = true;
                dfs(next.node, cost + next.cost);
            }
        }
    }   
}

class Node {
    int node, cost;
    
    public Node(int node, int cost) {
        this.node = node;
        this.cost = cost;
    }
}