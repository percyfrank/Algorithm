import java.io.*;
import java.util.*;

public class Main {

    static StringTokenizer st;
    static int n, m, years;
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
            adjustHeight();
            years += 1;
            
            int cnt = 0;
            visited = new boolean[n][m];
            if(checkIce()) {
                for (int i = 1; i < n-1 ; i++) {
                    for (int j = 1; j < m-1 ; j++) {
                        if(!visited[i][j] && graph[i][j] != 0) {
                            bfs(i,j);
                            cnt += 1;
                            if(cnt >= 2) {
                                System.out.println(years);
                                return;
                            }
                        }
                    }
                }
            } else {
                System.out.println(0);
                return;
            }
        }        
    }

    public static boolean isRange(int x, int y) {
        return x >= 0 && x < n && y >= 0 && y < m;
    }
    
    public static void adjustHeight() {
        
        int[][] height = new int[n][m];
        
        for (int i = 1; i < n-1 ; i++) {
            for (int j = 1; j < m-1 ; j++) {
                if (graph[i][j] != 0) {
                    for(int k = 0; k < 4; k ++) {
                        int ni = i + dx[k];
                        int nj = j + dy[k];
                        if(isRange(ni, nj) && graph[ni][nj] == 0) {
                            height[i][j] += 1;
                        }
                    }
                }
            }
        }
        
        for (int i = 1; i < n-1 ; i++) {
            for (int j = 1; j < m-1 ; j++) {
                graph[i][j] -= height[i][j];
                if (graph[i][j] <= 0) {
                    graph[i][j] = 0;
                }
            }
        }
    }
    
    public static boolean checkIce() {
        
        for (int i = 1; i < n-1 ; i++) {
            for (int j = 1; j < m-1 ; j++) {
                if (graph[i][j] != 0) {
                    return true;
                }
            }
        }        
        return false;
    }

    public static void bfs(int x, int y) {

        Queue<Point> q = new LinkedList<>();
        q.offer(new Point(x,y));
        visited[x][y] = true;

        while(!q.isEmpty()) {
            Point p = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];
                if (!isRange(nx, ny) || visited[nx][ny] || graph[nx][ny] == 0) continue;
                if(!visited[nx][ny] && graph[nx][ny] != 0) {
                    visited[nx][ny] = true;
                    q.offer(new Point(nx,ny));
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