import java.io.*;
import java.util.*;

public class Main {

    static StringTokenizer st;
    static int n, m;
    static int[][] maze;
    static int[][] visited;
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        maze = new int[n][m];
        visited = new int[n][m];
        for (int i = 0; i < n; i++) {
            String tmp = br.readLine();
            for (int j = 0; j < tmp.length(); j++) {
                maze[i][j] = Integer.parseInt(String.valueOf(tmp.charAt(j)));
            }
        }

        bfs(0, 0);
        System.out.println(visited[n - 1][m - 1]);

    }

    static void bfs(int x, int y) {

        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{x, y});
        visited[x][y] = 1;

        while (!q.isEmpty()) {
            int[] tmp = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = tmp[0] + dx[i];
                int ny = tmp[1] + dy[i];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (maze[nx][ny] == 1 && visited[nx][ny] == 0) {
                        visited[nx][ny] = visited[tmp[0]][tmp[1]] + 1;
                        q.offer(new int[]{nx, ny});
                    }
                }
            }
        }
    }
}