import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        List<Integer> towers = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            towers.add(Integer.parseInt(st.nextToken()));
        }
        Collections.reverse(towers);

        Deque<int[]> stack = new ArrayDeque<>();
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && stack.peekLast()[1] < towers.get(i)) {
                int[] tmp = stack.pollLast();
                int idx = tmp[0];
                int prev = tmp[1];
                ans[idx] = n - i;
            }

            stack.add(new int[]{i, towers.get(i)});
        }

        StringBuilder sb = new StringBuilder();
        for (int i = n-1; i >= 0; i--) {
            sb.append(ans[i]).append(" ");
        }

        System.out.println(sb.toString());

    }
}