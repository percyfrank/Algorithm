import java.io.*;
import java.util.*;

public class Main {

    static StringTokenizer st;
    static int n, m, h, w, Sr, Sc, Fr, Fc, ans;
    static int[][] graph;
    static boolean[][] visited;
    static List<int[]> wall = new ArrayList<>();
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new int[n][m];
        visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                if(graph[i][j] == 1) {
                    wall.add(new int[] {i,j});
                }
            }
        }
        st = new StringTokenizer(br.readLine());
        h = Integer.parseInt(st.nextToken());
        w = Integer.parseInt(st.nextToken());
        Sr = Integer.parseInt(st.nextToken()) - 1;
        Sc = Integer.parseInt(st.nextToken()) - 1;
        Fr = Integer.parseInt(st.nextToken()) - 1;
        Fc = Integer.parseInt(st.nextToken()) - 1;
        
        ans = bfs(Sr,Sc,0);
        System.out.println(ans);
    }

    public static boolean isRange(int x, int y) {
        return x >= 0 && x < n && y >= 0 && y < m;
    }

    public static int bfs(int x, int y, int dist) {

        Queue<Point> q = new LinkedList<>();
        q.offer(new Point(x,y,dist));
        visited[x][y] = true;

        while(!q.isEmpty()) {
            Point p = q.poll();
            if(p.x == Fr && p.y == Fc) {
                return p.dist;
            }
            for (int i = 0; i < 4; i++) {
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];
                if(!isRange(nx,ny) || !isPossible(nx,ny) || visited[nx][ny]) continue;                    
                if(!visited[nx][ny]) {
                    visited[nx][ny] = true;
                    q.offer(new Point(nx,ny,p.dist+1));
                }
            }
        }
        return -1;
    }
    
    public static boolean isPossible(int x, int y) {
        
        int bx = x + h - 1;
        int by = y + w - 1;
        
        if(bx < 0 || by < 0 || bx >= n || by >= m) {
            return false;
        }
        for(int i = 0; i < wall.size(); i++) {
            int wallX = wall.get(i)[0];
            int wallY = wall.get(i)[1];
            if(wallX >= x && wallX <= bx && wallY >= y && wallY <= by) {
                return false;
            }
        }
        
        return true;        
    }
}

class Point {
    int x,y,dist;
    
    public Point(int x, int y, int dist) {
        this.x = x;
        this.y = y;
        this.dist = dist;
    }
}