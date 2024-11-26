import java.io.*;
import java.util.*;

public class Main {
    
    static StringTokenizer st;
    static int m,n,h;
    static int[][][] graph;
    static int[] dx = {0,1,0,-1,0,0};
    static int[] dy = {1,0,-1,0,0,0};
    static int[] dz = {0,0,0,0,1,-1};
    static Queue<Point> q = new LinkedList<>();
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());
        graph = new int[h][n][m];
        
        int cnt = 0;
        for (int k=0; k<h; k++) {
            for (int i=0; i<n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j=0; j<m; j++) {
                    graph[k][i][j] = Integer.parseInt(st.nextToken());
                    if (graph[k][i][j] == 1) {
                        cnt += 1;
                        q.offer(new Point(i,j,k));
                    }
                }
            }
        }
        if(cnt == m*n*h) {
            System.out.println(0);
            return;
        }
        
        bfs();
        
        int ans = 0;
        for (int k=0; k<h; k++) {
            for (int i=0; i<n; i++) {
                for (int j=0; j<m; j++) {
                    if (graph[k][i][j] == 0) {
                        System.out.println(-1);
                        return;
                    }
                    if(graph[k][i][j] == -1) continue;
                    ans = Math.max(ans,graph[k][i][j]);
                }
            }
        }
        System.out.println(ans-1);
    }
    
    public static void bfs() {

        while(!q.isEmpty()) {
            Point p = q.poll();
            for (int i=0; i<6; i++) {
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];
                int nz = p.z + dz[i];
                if(nx < 0 || nx >= n || ny < 0 || ny >= m || nz < 0 || nz >= h || graph[nz][nx][ny] == -1 || graph[nz][nx][ny] == 1) {
                    continue;
                }
                if(graph[nz][nx][ny] == 0 || graph[p.z][p.x][p.y] + 1 < graph[nz][nx][ny]) {
                    q.offer(new Point(nx,ny,nz));
                    graph[nz][nx][ny] = graph[p.z][p.x][p.y] + 1;
                }
            }
        }
    }
}

class Point {
    int x,y,z;
    public Point(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
}