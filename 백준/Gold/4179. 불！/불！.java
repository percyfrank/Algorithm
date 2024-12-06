import java.io.*;
import java.util.*;

public class Main {

    static StringTokenizer st;
    static int r,c,sX,sY,ans;
    static Queue<Point> q = new LinkedList<>();
    static char[][] graph;
    static int[][] fire, human;
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        graph = new char[r][c];
        fire = new int[r][c];

        for (int i = 0; i < r; i++) {
            String tmp = br.readLine();
            for (int j = 0; j < c; j++) {
                graph[i][j] = tmp.charAt(j);
                if(graph[i][j] == 'J') {
                    sX = i;
                    sY = j;
                }
                if(graph[i][j] == 'F') {
                    q.offer(new Point(i,j));
                    fire[i][j] = 1;
                }
            }
        }
                
        bfs();
        human = new int[r][c];
        ans = checkFire(sX,sY);
        if(ans == -1) {
            System.out.println("IMPOSSIBLE");
        } else {
            System.out.println(ans);
        }
    }

    public static boolean isRange(int x, int y) {
        return x >= 0 && x < r && y >= 0 && y < c;
    }
    
    public static void bfs() {

        while(!q.isEmpty()) {
            Point p = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];
                if (!isRange(nx, ny) || graph[nx][ny] == '#') continue;
                if(fire[nx][ny] == 0) {
                    fire[nx][ny] = fire[p.x][p.y] + 1;
                    q.offer(new Point(nx,ny));
                }
            }
        }
    }

    public static int checkFire(int x, int y) {

        Queue<Point> q = new LinkedList<>();
        q.offer(new Point(x,y));
        human[x][y] = 1;

        while(!q.isEmpty()) {
            Point n = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = n.x + dx[i];
                int ny = n.y + dy[i];
                if(!isRange(nx,ny)) {
                    return human[n.x][n.y];
                }           
                if (graph[nx][ny] == '#')
                    continue;
                if (human[nx][ny] == 0  && (human[n.x][n.y] < fire[nx][ny] - 1 || fire[nx][ny] == 0)) {
                    human[nx][ny] = human[n.x][n.y] + 1;
                    q.offer(new Point(nx,ny));
                }
                    
            }
        }
        return -1;
    }
}

class Point {
    int x,y;
    
    public Point(int x,int y) {
        this.x = x;
        this.y = y;
    }
}