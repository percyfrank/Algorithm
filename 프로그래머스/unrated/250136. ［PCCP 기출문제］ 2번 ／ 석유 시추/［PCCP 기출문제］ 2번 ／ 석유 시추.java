import java.util.*;
import java.lang.Math;

class Point {
    public int x,y;
    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Solution {
        
    static int[] dx = {0,1,0,-1};
    static int[] dy = {1,0,-1,0};
    static int[][] visited;
    static int[] total;
    
    public int solution(int[][] land) {
        
        int row = land.length; 
        int col = land[0].length;
    
        total = new int[col]; // 가장 많은 석유량
        visited = new int[row][col];
        
        for (int i=0; i<row; i++) {            
            for(int j=0; j<col; j++) {
                if(land[i][j] == 1 && visited[i][j] == 0) {                    
                    bfs(i,j,land);
                }              
            }
        }
        
        // for (int i=0; i<col; i++) {
        //     System.out.println(total[i]);
        // }
        
        return Arrays.stream(total).max().getAsInt();
    }
    
    public void bfs(int x, int y, int[][] land) {
        
        int cnt = 0;
        visited[x][y] = 1;
        Queue<Point> q = new LinkedList<>();
        q.offer(new Point(x,y));
        int min_y = y;
        int max_y = y;
        
        while (!q.isEmpty()) {
            Point p = q.poll();
            min_y = Math.min(min_y, p.y);
            max_y = Math.max(max_y, p.y);
            cnt += 1;
            for (int i=0; i<4; i++) {
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];
                if(nx<0 || ny<0 || nx>=land.length || ny>=land[0].length) {
                    continue;
                }
                if(visited[nx][ny] == 0 && land[nx][ny] == 1) {
                    visited[nx][ny] = 1;
                    q.offer(new Point(nx,ny));
                }
            }
        }
        
        for (int i=min_y; i<=max_y; i++) {
            total[i] += cnt;
        }
    }
    

}