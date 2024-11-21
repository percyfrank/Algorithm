import java.io.*;
import java.util.*;

public class Main {

    static StringTokenizer st;
    static int n, k;
    static int[] visited = new int[100001];
    static int MIN = Integer.MAX_VALUE;
    static List<Integer> cnt = new ArrayList<>();


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        bfs(n, 0);
        System.out.println(MIN);
        int ans = 0;
        for(int i=0; i<cnt.size(); i++) {
            if (cnt.get(i) == MIN) {
                ans += 1;
            }
        }
        System.out.println(ans);
    }

    public static void bfs(int pos, int time) {

        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(pos, time));

        while (!q.isEmpty()) {
            Node n = q.poll();
            visited[n.pos] = 1;
            if (n.pos == k) {
                cnt.add(n.time);
                MIN = Math.min(MIN, n.time);
            }

            if (n.pos * 2 <= 100000 && visited[n.pos * 2] == 0) {
                q.offer(new Node(n.pos * 2, n.time + 1));
            }
            if (n.pos + 1 <= 100000 && visited[n.pos + 1] == 0) {
                q.offer(new Node(n.pos + 1, n.time + 1));
            }
            if (n.pos - 1 >= 0 && visited[n.pos - 1] == 0) {
                q.offer(new Node(n.pos - 1, n.time + 1));
            }
        }
    }
}

class Node {
    int pos, time;

    public Node(int pos, int time) {
        this.pos = pos;
        this.time = time;
    }
}