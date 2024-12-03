import java.io.*;
import java.util.*;

public class Main {

    static StringTokenizer st;
    static int n, m, time, ans;
    static int[][] graph;
    static boolean[][] visited;
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new int[n][m];        

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        
        while (true) {
            if(checkCheese()) {
                break;
            }
            visited = new boolean[n][m];
            ans = countCheese();
            bfs();
            time += 1;
        }
        
        System.out.println(time);
        System.out.println(ans);
    }

    public static boolean isRange(int x, int y) {
        return x >= 0 && x < n && y >= 0 && y < m;
    }
    
    public static int countCheese() {
        
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 1) {
                    cnt += 1;
                }
            }
        }
        return cnt;
    }
    
    public static boolean checkCheese() {
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 1) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void bfs() {

        Queue<Point> q = new LinkedList<>();
        q.offer(new Point(0,0));
        visited[0][0] = true;

        while(!q.isEmpty()) {
            Point p = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];
                if(!isRange(nx,ny)) continue;
                if(!visited[nx][ny]) {
                    if (graph[nx][ny] == 1) {
                        graph[nx][ny] = 0;
                        visited[nx][ny] = true;
                    }
                    else if (graph[nx][ny] == 0) {
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
    
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}