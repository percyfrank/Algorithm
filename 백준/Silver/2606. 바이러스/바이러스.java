import java.io.*;
import java.util.*;

public class Main {

    static int[][] graph;
    static boolean[] visited;
    static int n,m;
    static int cnt;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        graph = new int[n+1][n+1];
        visited = new boolean[n+1];
        StringTokenizer st;
        for(int i=0; i<m; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            graph[x][y] = graph[y][x] = 1;
        }

        System.out.println(bfs(1));

    }

    public static int bfs(int start) {

        Queue<Integer> q = new LinkedList<>();
        visited[start] = true;
        q.offer(start);

        while (!q.isEmpty()) {
            int tmp = q.poll();
            for (int i=1; i<=n; i++) {
                if(graph[tmp][i] == 1 && !visited[i]) {
                    q.offer(i);
                    visited[i] = true;
                    cnt++;
                }
            }

        }
        return cnt;
    }

}