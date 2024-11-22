import java.io.*;
import java.util.*;

public class Main {

    static StringTokenizer st;
    static int n,k;
    static int[] visited = new int[100001];
    static int cnt;
    static int min = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        
        if (n >= k) {
            System.out.println(n-k);
            System.out.println(1);
        } else {
            bfs(n);
            System.out.println(min);
            System.out.println(cnt);
        }
    }
    
    public static void bfs(int pos) {
        
        Queue<Integer> q = new LinkedList<>();
        q.offer(pos);
        visited[pos] = 1;
        
        while (!q.isEmpty()) {
            int curr = q.poll();
            if(min < visited[curr]) {
                return;
            }
            for(int i = 0; i < 3; i++) {
                int next;
                if (i == 0) next = curr + 1;
                else if (i == 1) next = curr - 1;
                else next = curr * 2;
                
                if (next < 0 || next > 100000) {
                    continue;
                }
                if(next == k) {
                    min = visited[curr];
                    cnt += 1;
                }
                if(visited[next] == 0 || visited[next] == visited[curr] + 1) {
                    visited[next] = visited[curr] + 1;
                    q.offer(next);
                }
                
            }
        }
    }
}