import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N,M,V;
    static ArrayList<ArrayList<Integer>> list;
    static boolean[] visited;
    static StringBuffer sb = new StringBuffer();

    public static void DFS(int start) {
        visited[start] = true;
        sb.append(start).append(" ");

        for (int i = 0; i < list.get(start).size(); i++) {
            if(!visited[list.get(start).get(i)]) {
                DFS(list.get(start).get(i));
            }
        }
    }

    public static void BFS(int start) {
        Queue<Integer> queue = new LinkedList<>();

        queue.add(start);
        visited[start] = true;

        while(!queue.isEmpty()) {
            int now = queue.poll();
            sb.append(now).append(" ");
            for (int i = 0; i < list.get(now).size(); i++) {
                if(!visited[list.get(now).get(i)]) {
                    queue.add(list.get(now).get(i));
                    visited[list.get(now).get(i)] = true;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());   // 정점 개수
        M = Integer.parseInt(st.nextToken());   // 간선 개수
        V = Integer.parseInt(st.nextToken());   // 시작 정점 번호

        list = new ArrayList<ArrayList<Integer>>();

        for (int i = 0; i <= N; i++) {
            list.add(new ArrayList<Integer>());
        }

        for (int i = 1; i <= M; i++) {
            st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());

            list.get(v1).add(v2);
            list.get(v2).add(v1);
        }

        for (int i = 1; i <= N; i++) {
            Collections.sort(list.get(i));
        }

        visited = new boolean[N + 1];
        DFS(V);
        Arrays.fill(visited, false);
        sb.append("\n");
        BFS(V);
        System.out.print(sb);

    }
}