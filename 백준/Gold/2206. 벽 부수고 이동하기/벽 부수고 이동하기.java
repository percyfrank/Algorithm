import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * 벽 부수고 이동하기 - 2206번
 */
public class Main {

    static int N,M;
    static int[][] map;
    static int[][] visited;
    static int[] dx = {-1,1,0,0}; // 상 하 좌 우
    static int[] dy = {0,0,-1,1};

    static class Point {
        int x;
        int y;
        int cnt;    // 거리
        int wall;   // 벽 뚫는 횟수

        public Point(int x, int y, int cnt, int wall) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
            this.wall = wall;
        }
    }
    public static int BFS(int x, int y) {
//        int wall = 1;
        Queue<Point> q = new LinkedList<>();

        q.add(new Point(x, y,1,0));
        visited[x][y] = 0;

        while(!q.isEmpty()) {
            Point p = q.remove();

            if(p.x == N-1 && p.y == M-1) {
                return p.cnt;
            }

            for (int i = 0; i < 4; i++) {
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];

                if(nx < 0 || ny < 0 || nx >= N || ny >= M) continue;

                if(visited[nx][ny] <= p.wall) continue;

                // 벽이 아닐 때
                if (map[nx][ny] == 0) {
                    visited[nx][ny] = p.wall;
                    q.add(new Point(nx,ny,p.cnt+1,p.wall));
                }
                // 벽일 때
                else {
                    if(p.wall == 0) {
                        visited[nx][ny] = p.wall + 1;
                        q.add(new Point(nx, ny,p.cnt+1,p.wall+1));
                    }
                }
            }
        }
        return -1;
    }


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[N][M];
        visited = new int[N][M];
        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            for (int j = 0; j < M; j++) {
                map[i][j] = s.charAt(j) - '0';
                visited[i][j] = Integer.MAX_VALUE;
            }
        }

        int result = BFS(0, 0);

        System.out.println(result);
    }
}