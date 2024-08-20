import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;

        Deque<Integer> list = new ArrayDeque<>();
        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            if (st.countTokens() == 1) {
                String command = st.nextToken();
                if (command.equals("front")) {
                    sb.append(list.isEmpty() ? -1 : list.peekFirst()).append("\n");
                } else if (command.equals("back")) {
                    sb.append(list.isEmpty() ? -1 : list.peekLast()).append("\n");
                } else if (command.equals("empty")) {
                    sb.append(list.isEmpty() ? 1 : 0).append("\n");
                } else if (command.equals("size")) {
                    sb.append(list.size()).append("\n");
                } else if (command.equals("pop_front")) {
                    sb.append(list.isEmpty() ? -1 : list.pollFirst()).append("\n");
                } else if (command.equals("pop_back")) {
                    sb.append(list.isEmpty() ? -1 : list.pollLast()).append("\n");
                }
            } else {
                String command = st.nextToken();
                int cnt = Integer.parseInt(st.nextToken());
                if(command.equals("push_front")) {
                    list.offerFirst(cnt);
                } else if(command.equals("push_back")) {
                    list.offerLast(cnt);
                }
            }

        }

        System.out.println(sb.toString());

    }
}