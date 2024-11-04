import java.io.*;
import java.util.*;

public class Main {

    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    static int n,m;
    static int cnt;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        graph = new ArrayList[n+1];
        for(int i=0; i<=n; i++) {
            graph[i] = new ArrayList<>();
        }
        visited = new boolean[n+1];
        for(int i=0; i<m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            graph[x].add(y);
            graph[y].add(x);
        }

        System.out.println(dfs(1));

    }

    public static int dfs(int start) {

        visited[start] = true;
        for(int x : graph[start]) {
            if(!visited[x]) {
                cnt++;
                dfs(x);
            }
        }

        return cnt;
    }
}