import java.io.*;
import java.util.*;

public class Main {

    static StringTokenizer st;
    static int r,c,n;
    static char[][] graph;
    static int[][] bomb;
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        graph = new char[r][c];
        bomb = new int[r][c];
        
        for (int i = 0; i < r; i++) {
            String tmp = br.readLine();
            for (int j = 0; j < c; j++) {
                graph[i][j] = tmp.charAt(j);
                if(graph[i][j] == 'O') {
                    bomb[i][j] = 3;
                }
            }
        }
        
        int time = 1;
        while(time <= n) {
            
            if(time % 2 == 0) {
                for (int i = 0; i < r; i++) {
                    for (int j = 0; j < c; j++) {
                        if(graph[i][j] == '.') {
                            graph[i][j] = 'O';
                            bomb[i][j] = time + 3;
                        }
                    }
                }
            } else if(time % 2 == 1) {
                for (int i = 0; i < r; i++) {
                    for (int j = 0; j < c; j++) {
                        if(graph[i][j] == 'O' && bomb[i][j] == time) {
                            graph[i][j] = '.';
                            bomb[i][j] = 0;
                            for (int k = 0; k < 4; k++) {
                                int ni = i + dx[k];
                                int nj = j + dy[k];
                                if(ni < 0 || ni >= r || nj < 0 || nj >= c) {
                                    continue;
                                }
                                if(graph[ni][nj] == 'O' && bomb[ni][nj] != time) {
                                    graph[ni][nj] = '.';
                                    bomb[ni][nj] = 0;
                                }
                            }
                        }
                    }
                }
            }
            time += 1;
        }
        for(int i = 0; i < r; i++) {
            System.out.println(graph[i]);
        }
    }
}