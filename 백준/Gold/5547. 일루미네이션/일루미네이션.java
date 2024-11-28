import java.io.*;
import java.util.*;

public class Main {

    static StringTokenizer st;
    static int w, h, res;
    static int[][] graph;
    static boolean[][] visited;
    static int[] dx = {-1, 1, 0, 1, 0, -1, -1, 1};
    static int[] dy = {1, 1, 1, 0, -1, 0, -1, -1};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        w = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());
        graph = new int[h + 2][w + 2];
        visited = new boolean[h + 2][w + 2];

        for (int i = 1; i <= h; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= w; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        bfs(0,0);
        System.out.println(res);

    }

    public static boolean isRange(int x, int y) {
        return x >= 0 && x < h + 2 && y >= 0 && y < w + 2;
    }

    public static void bfs(int x, int y) {

        Queue<Point> q = new LinkedList<>();
        q.offer(new Point(x,y));
        visited[x][y] = true;

        while(!q.isEmpty()) {
            Point p = q.poll();
            if (p.x % 2 != 0) {
                for (int i = 0; i < 6; i++) {
                    int nx = p.x + dx[i];
                    int ny = p.y + dy[i];
                    if (!isRange(nx, ny)) continue;
                    if(graph[nx][ny] == 1) {
                        res += 1;
                    }
                    if(!visited[nx][ny] && graph[nx][ny] == 0) {
                        visited[nx][ny] = true;
                        q.offer(new Point(nx,ny));
                    }
                }
            } else {
                for (int i = 2; i < 8; i++) {
                    int nx = p.x + dx[i];
                    int ny = p.y + dy[i];
                    if (!isRange(nx, ny)) continue;
                    if(graph[nx][ny] == 1) {
                        res += 1;
                    }
                    if(!visited[nx][ny] && graph[nx][ny] == 0) {
                        visited[nx][ny] = true;
                        q.offer(new Point(nx,ny));
                    }
                }
            }
        }
    }
}

class Point {
    int x,y;
    
    public Point(int x,int y) {
        this.x = x;
        this.y = y;
    }
}