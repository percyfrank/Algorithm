import java.io.*;
import java.util.*;

public class Main {
    
    static StringTokenizer st;
    static int n,l,r;
    static int[][] country;
    static int[][] visited;
    static int[] dx = {0,1,0,-1};
    static int[] dy = {1,0,-1,0};
    static List<Point> ally;
    
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        country = new int[n][n];        
        
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                country[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        
        int days = 0;
        while (true) {
            visited = new int[n][n];
            boolean flag = true;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if(visited[i][j] == 0) {
                        int population = bfs(i,j);
                        if(ally.size() > 1) {
                            changePopulation(population);
                            flag = false;
                        }
                    }
                }
            }
            if(flag) {
                System.out.println(days);
                break;
            }
            days++;
        }
    }
    
    public static int bfs(int x, int y) {
        
        Queue<Point> q = new LinkedList<>();
        ally = new ArrayList<>();
        q.offer(new Point(x,y));
        ally.add(new Point(x,y));
        visited[x][y] = 1;
        
        int sum = country[x][y];
        while(!q.isEmpty()) {
            Point p = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];
                if(nx < 0 || nx >= n || ny < 0 || ny >= n || Math.abs(country[p.x][p.y] - country[nx][ny]) < l || Math.abs(country[p.x][p.y] - country[nx][ny]) > r) {
                    continue;
                }
                if(visited[nx][ny] == 0) {
                    visited[nx][ny] = 1;
                    q.offer(new Point(nx,ny));
                    ally.add(new Point(nx,ny));
                    sum += country[nx][ny];
                }
            }
        }
        
        return sum;
    }
    
    public static void changePopulation(int population) {
        
        population = population / ally.size();
        for(int i = 0; i < ally.size(); i++) {
            Point p = ally.get(i);
            country[p.x][p.y] = population;
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