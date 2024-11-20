import java.io.*;
import java.util.*;

public class Main {

    static StringTokenizer st;
    static StringBuilder sb;
    static int n, m;
    static int[][] graph;
    static int[][] visited;
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static int targetX, targetY;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new int[n][m];
        visited = new int[n][m];
        
        for (int i = 0; i < n; i++) {
            String[] tmp = br.readLine().split(" ");
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(tmp[j]);
                if (graph[i][j] == 2) {
                    targetX = i;
                    targetY = j;
                }
            }
        }

        bfs(targetX, targetY);
        sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 2) {
                    sb.append(0).append(" ");
                    continue;
                }
                if(graph[i][j] != 0 && visited[i][j] == 0) {
                    sb.append(-1).append(" ");
                    continue;
                }
                sb.append(visited[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb.toString());
    }

    static void bfs(int x, int y) {

        Queue<Point> q = new LinkedList<>();
        q.offer(new Point(x,y));
        visited[x][y] = 0;

        while (!q.isEmpty()) {
            Point p = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (graph[nx][ny] == 1 && visited[nx][ny] == 0) {
                        visited[nx][ny] = visited[p.x][p.y] + 1;
                        q.offer(new Point(nx, ny));
                    }
                }
            }
        }
    }
}

class Point {
    int x,y;
    
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}