import java.io.*;
import java.util.*;

public class Main {
    
    static StringTokenizer st;
    static int m,n;
    static int[][] graph;
    static int[] dx = {0,1,0,-1};
    static int[] dy = {1,0,-1,0};
    static Queue<Point> q = new LinkedList<>();
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        graph = new int[n][m];
        
        List<Point> tomato = new ArrayList<>();
        int cnt = 0;
        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                if (graph[i][j] == 1) {
                    cnt += 1;
                    q.offer(new Point(i,j));
                }
            }
        }
        if(cnt == m*n) {
            System.out.println(0);
            return;
        }
        
        bfs();
        
        int ans = 0;
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                if (graph[i][j] == 0) {
                    System.out.println(-1);
                    return;
                }
                if( graph[i][j] == -1) continue;
                ans = Math.max(ans,graph[i][j]);
            }
        }        
        System.out.println(ans-1);
    }
    
    public static void bfs() {

        while(!q.isEmpty()) {
            Point p = q.poll();
            for (int i=0; i<4; i++) {
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];
                if(nx < 0 || nx >= n || ny < 0 || ny >= m || graph[nx][ny] == -1 || graph[nx][ny] == 1) {
                    continue;
                }
                if(graph[nx][ny] == 0 || graph[p.x][p.y] + 1 < graph[nx][ny]) {
                    q.offer(new Point(nx,ny));
                    graph[nx][ny] = graph[p.x][p.y] + 1;
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