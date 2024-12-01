import java.io.*;
import java.util.*;

public class Main {

    static StringTokenizer st;
    static int n, k;
    static long ans;
    static Set<Integer> visited = new HashSet<>();
    static int[] dx = {1, -1};
    static Queue<Node> q = new LinkedList<>();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(st.nextToken());
            q.add(new Node(x,0));
            visited.add(x);
        }

        bfs();
        System.out.println(ans);
    }

    public static void bfs() {

        int cnt = 0;
        while (!q.isEmpty()) {
            Node n = q.poll();
            for (int i = 0; i < 2; i++) {
                int nx = n.x + dx[i];
                if(visited.contains(nx)) continue;

                ans += n.dist + 1;
                cnt += 1;
                visited.add(nx);

                if(cnt == k) {
                    return;
                }
                q.offer(new Node(nx,n.dist+1));
            }
        }
    }
}

class Node {
    int x, dist;

    public Node(int x, int dist) {
        this.x = x;
        this.dist = dist;
    }
}