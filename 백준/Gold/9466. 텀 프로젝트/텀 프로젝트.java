import java.io.*;
import java.util.*;

public class Main {

    static StringTokenizer st;
    static int t, n, ans;
    static int[] students;
    static boolean[] visited, done;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            n = Integer.parseInt(br.readLine());
            students = new int[n + 1];
            visited = new boolean[n + 1];
            done = new boolean[n + 1];

            st = new StringTokenizer(br.readLine());
            ans = 0;
            for (int j = 1; j <= n; j++) {
                students[j] = Integer.parseInt(st.nextToken());
                if(j == students[j]) {
                    done[j] = true;
                    ans += 1;
                }
            }

            for (int k = 1; k <= n; k++) {
                if(!done[k]) {
                    dfs(k);
                }
            }
            System.out.println(n-ans);
        }
    }

    public static void dfs(int start) {

        if(visited[start]) {
            done[start] = true;
            ans += 1;
        } else {
            visited[start] = true;
        }

        int next = students[start];
        if(!done[next]) {
            dfs(next);
        }

        visited[start] = false;
        done[start] = true;
    }
}