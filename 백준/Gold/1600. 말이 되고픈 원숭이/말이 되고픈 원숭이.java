import java.io.*;
import java.util.*;

public class Main {

    static StringTokenizer st;
    static int k, w, h;    
    static int[][] graph;
    static boolean[][][] visited;
    static int[] dx = {0, 1, 0, -1};    
    static int[] dy = {1, 0, -1, 0};
    static int[] hx = {-2, -1, 1, 2, 2, 1, -1, -2};
    static int[] hy = {1, 2, 2, 1, -1, -2, -2, -1};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        k = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        w = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());
        graph = new int[h][w];
        visited = new boolean[h][w][k+1];

        for (int i = 0; i < h; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < w; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        
        System.out.println(bfs());
    }

    public static boolean isRange(int x, int y) {
        return x >= 0 && x < h && y >= 0 && y < w;
    }
    
    public static int bfs() {
        
        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(0, 0, 0, 0));
        visited[0][0][0] = true;

        while(!q.isEmpty()) {
            Node n = q.poll();
            if(n.x == h-1 && n.y == w-1) {
                return n.move;
            }
            for (int i = 0; i < 4; i++) {
                int nx = n.x + dx[i];
                int ny = n.y + dy[i];
                if (!isRange(nx, ny) || graph[nx][ny] == 1 || visited[nx][ny][n.cnt]) continue;
                visited[nx][ny][n.cnt] = true;
                q.offer(new Node(nx, ny, n.cnt, n.move+1));
            }
            if(n.cnt < k) {
                for (int i = 0; i < 8; i++) {
                    int nx = n.x + hx[i];
                    int ny = n.y + hy[i];
                    int nCnt = n.cnt + 1;
                    if (!isRange(nx, ny) || graph[nx][ny] == 1 || visited[nx][ny][nCnt]) continue;
                    visited[nx][ny][nCnt] = true;
                    q.offer(new Node(nx, ny, nCnt, n.move+1));
                }
            }
        }
        return -1;
    }
}

class Node {
    int x, y, cnt, move;
    
    public Node(int x, int y, int cnt, int move) {
        this.x = x;
        this.y = y;
        this.cnt = cnt;
        this.move = move;
    }
}