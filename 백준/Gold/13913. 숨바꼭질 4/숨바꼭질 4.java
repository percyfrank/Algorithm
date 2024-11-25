import java.io.*;
import java.util.*;

public class Main {

    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    static int n, k;
    static boolean[] visited = new boolean[100001];
    static int[] route = new int[100001];
    static int ans = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        bfs(n, 0);
        Stack<Integer> stack = new Stack<>();
        stack.push(k);
        int prev = k;
        while (prev != n) {
            stack.push(route[prev]);
            prev = route[prev];
        }
        
        System.out.println(ans);
        while (!stack.isEmpty()) {
            sb.append(stack.pop()).append(" ");
        }
        System.out.println(sb.toString());
    }

    public static void bfs(int pos, int time) {

        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(pos, time));
        visited[pos] = true;

        while (!q.isEmpty()) {
            Node n = q.poll();
            int currPos = n.pos;
            int currTime = n.time;

            if (currPos == k) {
                ans = Math.min(ans, currTime);
                break;
            }

            if (currPos * 2 <= 100_000 && !visited[currPos * 2]) {                
                q.offer(new Node(currPos * 2, currTime + 1));
                route[currPos * 2] = currPos;
                visited[currPos * 2] = true;                
            }
            if (currPos + 1 <= 100_000 && !visited[currPos + 1]) {
                q.offer(new Node(currPos + 1, currTime + 1));
                route[currPos + 1] = currPos;
                visited[currPos + 1] = true;
            }
            if (currPos - 1 >= 0 && !visited[currPos - 1]) {
                q.offer(new Node(currPos - 1, currTime + 1));
                route[currPos - 1] = currPos;
                visited[currPos - 1] = true;
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