import java.io.*;
import java.util.*;

public class Main {

    static StringTokenizer st;
    static StringBuilder sb;
    static int n;
    static int[][] graph;
    static int[][] visited;
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new int[n][n];
        visited = new int[n][n];
        
        for (int i = 0; i < n; i++) {
            String tmp = br.readLine();
            for (int j = 0; j < n; j++) {
                graph[i][j] = tmp.charAt(j) - '0';                
            }
        }

        List<Integer> houseCnt = new ArrayList<>();        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (graph[i][j] == 1 && visited[i][j] == 0) {
                    houseCnt.add(bfs(i,j));
                }
            }
        }
        
        sb = new StringBuilder();
        sb.append(houseCnt.size()).append("\n");
        Collections.sort(houseCnt);
        for (int i = 0; i < houseCnt.size(); i++) {
            sb.append(houseCnt.get(i)).append("\n");
        }
        System.out.println(sb.toString());
    }

    static int bfs(int x, int y) {

        Queue<Point> q = new LinkedList<>();
        q.offer(new Point(x,y));
        visited[x][y] = 1;
        int cnt = 1;

        while (!q.isEmpty()) {
            Point p = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];
                if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                    if (graph[nx][ny] == 1 && visited[nx][ny] == 0) {
                        visited[nx][ny] = 1;
                        cnt += 1;
                        q.offer(new Point(nx, ny));
                    }
                }
            }
        }        
        return cnt;
    }
}

class Point {
    int x,y;
    
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}