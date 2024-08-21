import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        Deque<Balloon> deque = new ArrayDeque<>();
        for (int i = 1; i <= n; i++) {
            deque.add(new Balloon(i, Integer.parseInt(st.nextToken())));
        }

        StringBuilder sb = new StringBuilder();

        while (!deque.isEmpty()) {
            sb.append(deque.peekFirst().idx + " ");
            int next = deque.pollFirst().val;

            if (deque.isEmpty()) {
                break;
            }

            if (next > 0) {
                for (int i = 0; i < next - 1; i++) {
                    deque.addLast(deque.pollFirst());
                }
            } else {
                for (int i = 0; i < Math.abs(next); i++) {
                    deque.addFirst(deque.pollLast());
                }
            }
        }

        System.out.println(sb.toString());

    }

}

class Balloon {
    int idx, val;

    public Balloon(int idx, int val) {
        this.idx = idx;
        this.val = val;
    }
}