import java.io.*;
import java.util.*;

public class Main {
    
    static StringTokenizer st;
    static int n,m,t;
    static int[][] graph;
    static int[][] visited;
    static int[] dx = {0,1,0,-1};
    static int[] dy = {1,0,-1,0};
    static int swordX,swordY;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        t = Integer.parseInt(st.nextToken());
        graph = new int[n][m];
        visited = new int[n][m];
        
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                if (graph[i][j] == 2) {
                    swordX = i;
                    swordY = j;
                }
            }
        }
        
        bfs();        
        int time = visited[n-1][m-1];        
        int timeWithSword = visited[swordX][swordY];
        if(timeWithSword != 0) {
            timeWithSword += Math.abs((n-swordX-1) + (m-swordY-1));
        }
        
        int ans = 0;
        if(time == 0 && timeWithSword != 0) {
            ans = timeWithSword;
        } else if(time != 0 && timeWithSword == 0) {
            ans = time;
        } else {
            ans = Math.min(time,timeWithSword);
        }
        
        if(ans == 0 || ans > t) System.out.println("Fail");
        else System.out.println(ans);
    }
    
    public static void bfs() {
        
        Queue<Point> q = new LinkedList<>();
        q.offer(new Point(0,0));
        visited[0][0] = 0;
        
        while(!q.isEmpty()) {
            Point p = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];
                if(nx < 0 || nx >= n || ny < 0 || ny >= m || graph[nx][ny] == 1) {
                    continue;
                }
                if(visited[nx][ny] == 0) {                    
                    visited[nx][ny] = visited[p.x][p.y] + 1;
                    q.offer(new Point(nx,ny));
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